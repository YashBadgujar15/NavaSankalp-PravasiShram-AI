try {
    $pptApp = New-Object -ComObject PowerPoint.Application
    $pres = $pptApp.Presentations.Open("C:\Users\ABCD\.gemini\antigravity-ide\scratch\navasankalp-shramsaathi\PravasiShram_AI_Flagship_Presentation.pptx", $true, $false, $false)
    $pres.SaveAs("C:\Users\ABCD\.gemini\antigravity-ide\scratch\navasankalp-shramsaathi\slide_export", 17)
    $pres.Close()
    $pptApp.Quit()
    Write-Host "Slides exported to PNG successfully!"
} catch {
    Write-Host "Error: " $_.Exception.Message
}
