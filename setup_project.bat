@echo off
echo ======================================================
echo   MIMO-AXON - AUTOMATIC PROJECT ORGANIZER
echo ======================================================
echo.

:: 1. Tao cau truc thu muc
echo [1/3] Dang tao cac thu muc module...
if not exist "docs\proposal" mkdir "docs\proposal"
if not exist "docs\planning" mkdir "docs\planning"
if not exist "docs\research" mkdir "docs\research"
if not exist "src\core" mkdir "src\core"
if not exist "src\modules\tts" mkdir "src\modules\tts"
if not exist "src\modules\dubbing" mkdir "src\modules\dubbing"
if not exist "data\input" mkdir "data\input"
if not exist "data\output" mkdir "data\output"
if not exist "web" mkdir "web"

:: 2. Di chuyen file vao dung vi tri
echo [2/3] Dang sap xep file vao dung module...

:: Documents - Proposal
if exist "XIAOMI_MIMO_PROPOSAL.md" move /Y "XIAOMI_MIMO_PROPOSAL.md" "docs\proposal\"
if exist "note.txt" move /Y "note.txt" "docs\proposal\"

:: Documents - Planning
if exist "PROJECT_PLAN.md" move /Y "PROJECT_PLAN.md" "docs\planning\"
if exist "USE_CASES_DETAILED.md" move /Y "USE_CASES_DETAILED.md" "docs\planning\"
if exist "ý tưởng.txt" move /Y "ý tưởng.txt" "docs\planning\"

:: Documents - Research
if exist "tiktok_audio.md" move /Y "tiktok_audio.md" "docs\research\"
if exist "tree.txt" move /Y "tree.txt" "docs\research\"
if exist "New Text Document.txt" move /Y "New Text Document.txt" "docs\research\"
if exist "*.png" move /Y "*.png" "docs\research\"

:: Source Code - Core
if exist "ocr_module_v1.py" move /Y "ocr_module_v1.py" "src\core\ocr_engine.py"

:: Source Code - Modules
if exist "TMF.py" move /Y "TMF.py" "src\modules\dubbing\"
if exist "TMF_GoogleTTS.py" move /Y "TMF_GoogleTTS.py" "src\modules\dubbing\"
if exist "TTS_API_Google.py" move /Y "TTS_API_Google.py" "src\modules\dubbing\"
if exist "TMF_Local_Engine" move /Y "TMF_Local_Engine" "src\modules\dubbing\"
if exist "VLC_AI_Dubber" move /Y "VLC_AI_Dubber" "src\modules\dubbing\"
if exist "fix_markdown.py" move /Y "fix_markdown.py" "src\modules\tts\"

:: Web Dashboard
if exist "DASHBOARD.html" move /Y "DASHBOARD.html" "web\index.html"

:: Data Assets
if exist "tiktok_audio.mp3" move /Y "tiktok_audio.mp3" "data\input\"
if exist "[VCB-Studio]*.*" move /Y "[VCB-Studio]*.*" "data\input\"

echo.
echo ======================================================
echo   DONE! Du an MIMO-AXON da duoc sap xep hoan hao.
echo ======================================================
pause
