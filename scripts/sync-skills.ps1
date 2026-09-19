# Maintenance only: replaces bundled skill copies from already available sources.
[CmdletBinding(SupportsShouldProcess)]
param()

$ErrorActionPreference = 'Stop'
$pluginRoot = [IO.Path]::GetFullPath((Join-Path $PSScriptRoot '..'))
$skillsRoot = [IO.Path]::GetFullPath((Join-Path $pluginRoot 'skills'))
$sources = [ordered]@{
    'angular-developer' = @('external/angular-skills/angular-developer', $null)
    'angular-bootstrap-italia' = @('external/angular-bootstrap-italia-skill/angular-bootstrap-italia', $null)
    'ponytail' = @('external/ponytail/skills/ponytail', 'external/ponytail/LICENSE')
    'caveman' = @('external/caveman/skills/caveman', 'external/caveman/LICENSE')
    'modern-css' = @('external/modern-css', $null)
    'web-typography' = @('external/wondelai-skills/web-typography', 'external/wondelai-skills/LICENSE')
}

# Validate every source and the resolved deletion boundaries before changing anything.
$jobs = foreach ($name in $sources.Keys) {
    $source = [IO.Path]::GetFullPath((Join-Path $pluginRoot $sources[$name][0]))
    $target = [IO.Path]::GetFullPath((Join-Path $skillsRoot $name))
    if (-not $target.StartsWith($skillsRoot + [IO.Path]::DirectorySeparatorChar,
            [StringComparison]::OrdinalIgnoreCase) -or
            [IO.Path]::GetDirectoryName($target) -ne $skillsRoot) {
        throw "Unsafe sync target: $target"
    }
    if (-not (Test-Path -LiteralPath (Join-Path $source 'SKILL.md') -PathType Leaf)) {
        throw "Missing source skill: $source. No bundled skills were changed."
    }
    foreach ($directory in @($skillsRoot, $target)) {
        if ((Test-Path -LiteralPath $directory) -and
                ((Get-Item -LiteralPath $directory -Force).Attributes -band [IO.FileAttributes]::ReparsePoint)) {
            throw "Refusing linked sync target: $directory"
        }
    }
    if (Test-Path -LiteralPath $target -PathType Container) {
        if (Get-ChildItem -LiteralPath $target -Force -Recurse |
                Where-Object { $_.Attributes -band [IO.FileAttributes]::ReparsePoint }) {
            throw "Refusing target containing links: $target"
        }
    }
    if (Get-ChildItem -LiteralPath $source -Force -Recurse |
            Where-Object { $_.Attributes -band [IO.FileAttributes]::ReparsePoint }) {
        throw "Refusing source containing links: $source"
    }
    $license = $null
    if ($sources[$name][1]) {
        $license = Join-Path $pluginRoot $sources[$name][1]
        if (-not (Test-Path -LiteralPath $license -PathType Leaf)) {
            throw "Missing upstream license: $license. No bundled skills were changed."
        }
    }
    [PSCustomObject]@{ Name = $name; Source = $source; Target = $target; License = $license }
}

foreach ($job in $jobs) {
    if ($PSCmdlet.ShouldProcess($job.Target, 'Replace bundled skill from verified local source')) {
        if (Test-Path -LiteralPath $job.Target) {
            Remove-Item -LiteralPath $job.Target -Recurse -Force
        }
        New-Item -ItemType Directory -Path $job.Target -Force | Out-Null
        # Source roots can be Git submodules. Never distribute their .git pointers.
        Get-ChildItem -LiteralPath $job.Source -Force |
            Where-Object { $_.Name -ne '.git' } |
            ForEach-Object { Copy-Item -LiteralPath $_.FullName -Destination $job.Target -Recurse -Force }
        if ($job.License) {
            Copy-Item -LiteralPath $job.License -Destination (Join-Path $job.Target 'LICENSE') -Force
        }
        Write-Host "Synced $($job.Name)"
    }
}
Write-Host 'Run scripts/validate-plugin.py and review the diff before distributing.'
