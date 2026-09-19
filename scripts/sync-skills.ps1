$ErrorActionPreference = "Stop"

Write-Host "Syncing Agent Skills..."

# ============================================================
# Sources
# ============================================================

$angularSource = "external\angular-skills\angular-developer"
$bootstrapItaliaSource = "external\angular-bootstrap-italia-skill\angular-bootstrap-italia"
$ponytailSource = "external\ponytail\skills\ponytail"
$cavemanSource = "external\caveman\skills\caveman"
$modernCssSource = "external\modern-css"
$webTypographySource = "external\wondelai-skills\web-typography"

# ============================================================
# Targets
# ============================================================

$angularTarget = "skills\angular-developer"
$bootstrapItaliaTarget = "skills\angular-bootstrap-italia"
$ponytailTarget = "skills\ponytail"
$cavemanTarget = "skills\caveman"
$modernCssTarget = "skills\modern-css"
$webTypographyTarget = "skills\web-typography"

$targets = @(
    $angularTarget,
    $bootstrapItaliaTarget,
    $ponytailTarget,
    $cavemanTarget,
    $modernCssTarget,
    $webTypographyTarget
)

# ============================================================
# Remove existing synced skills
# ============================================================

foreach ($target in $targets) {
    if (Test-Path $target) {
        Write-Host "Removing existing $target..."
        Remove-Item $target -Recurse -Force
    }
}

# ============================================================
# Validate sources
# ============================================================

if (-not (Test-Path $angularSource)) {
    throw "Angular skill not found at $angularSource"
}

if (-not (Test-Path $bootstrapItaliaSource)) {
    throw "Bootstrap Italia skill not found at $bootstrapItaliaSource"
}

if (-not (Test-Path $ponytailSource)) {
    throw "Ponytail skill not found at $ponytailSource"
}

if (-not (Test-Path $cavemanSource)) {
    throw "Caveman skill not found at $cavemanSource"
}

if (-not (Test-Path $modernCssSource)) {
    throw "Modern CSS skill not found at $modernCssSource"
}

if (-not (Test-Path $webTypographySource)) {
    throw "Web Typography skill not found at $webTypographySource"
}

# ============================================================
# Copy skills
# ============================================================

Write-Host "Copying angular-developer..."
Copy-Item `
    $angularSource `
    $angularTarget `
    -Recurse

Write-Host "Copying angular-bootstrap-italia..."
Copy-Item `
    $bootstrapItaliaSource `
    $bootstrapItaliaTarget `
    -Recurse

Write-Host "Copying ponytail..."
Copy-Item `
    $ponytailSource `
    $ponytailTarget `
    -Recurse

Write-Host "Copying caveman..."
Copy-Item `
    $cavemanSource `
    $cavemanTarget `
    -Recurse

Write-Host "Copying modern-css..."
Copy-Item `
    $modernCssSource `
    $modernCssTarget `
    -Recurse

Write-Host "Copying web-typography..."
Copy-Item `
    $webTypographySource `
    $webTypographyTarget `
    -Recurse

# ============================================================
# Final validation
# ============================================================

Write-Host ""
Write-Host "Validating synced skills..."

$skillFiles = @(
    "skills\angular-developer\SKILL.md",
    "skills\angular-bootstrap-italia\SKILL.md",
    "skills\ponytail\SKILL.md",
    "skills\caveman\SKILL.md",
    "skills\modern-css\SKILL.md",
    "skills\web-typography\SKILL.md"
)

foreach ($skillFile in $skillFiles) {
    if (-not (Test-Path $skillFile)) {
        throw "Synced skill is missing SKILL.md: $skillFile"
    }

    Write-Host "[OK] $skillFile"
}

Write-Host ""
Write-Host "Skills synced successfully."
Write-Host ""
Write-Host "Available skills:"
Write-Host " - angular-developer"
Write-Host " - angular-bootstrap-italia"
Write-Host " - ponytail"
Write-Host " - caveman"
Write-Host " - modern-css"
Write-Host " - web-typography"