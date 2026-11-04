import { createHash } from 'node:crypto';
import { access, mkdir, readFile, rm, writeFile } from 'node:fs/promises';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import { spawnSync } from 'node:child_process';

const root = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const version = '0.169.0';
const sha256 = '2d2f0bfe357d8cb4cec02f6bb28a3bff34978c8dda44b618029c5eb9d66765a7';
const toolDir = join(root, '.tools', `hugo-${version}`);
const binary = process.env.HUGO_BIN || join(toolDir, 'hugo');

function run(command, args, options = {}) {
  const result = spawnSync(command, args, { cwd: root, encoding: 'utf8', ...options });
  if (result.error) throw result.error;
  if (result.status !== 0) throw new Error(`${command} failed: ${result.stderr || result.stdout || result.status}`);
  return result;
}

try {
  try { await access(binary); }
  catch {
    if (process.env.HUGO_BIN || process.platform !== 'linux' || process.arch !== 'x64') {
      throw new Error(`Install Hugo ${version} and set HUGO_BIN to its executable path. Automatic installation supports Linux x64.`);
    }
    await mkdir(toolDir, { recursive: true });
    const url = `https://github.com/gohugoio/hugo/releases/download/v${version}/hugo_${version}_linux-amd64.tar.gz`;
    const response = await fetch(url);
    if (!response.ok) throw new Error(`Hugo download failed: HTTP ${response.status}`);
    const bytes = Buffer.from(await response.arrayBuffer());
    if (createHash('sha256').update(bytes).digest('hex') !== sha256) throw new Error('Hugo archive checksum mismatch');
    const archive = join(toolDir, 'hugo.tar.gz');
    await writeFile(archive, bytes);
    run('tar', ['-xzf', archive, '-C', toolDir, 'hugo']);
    await rm(archive);
  }
  const installed = run(binary, ['version']).stdout;
  if (!installed.startsWith(`hugo v${version} `) && !installed.startsWith(`hugo v${version}-`)) {
    throw new Error(`Expected Hugo ${version}; found ${installed.trim()}`);
  }
  await rm(join(root, 'dist'), { recursive: true, force: true });
  run(binary, ['--destination', 'dist', '--environment', 'production'], { stdio: 'inherit' });
  await access(join(root, 'dist', 'index.html'));
  console.log(`Built with verified Hugo ${version}.`);
} catch (error) {
  console.error(error.message);
  process.exitCode = 1;
}
