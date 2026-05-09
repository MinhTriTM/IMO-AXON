@echo off
echo ======================================================
echo   MIMO-AXON - GIT CLEAN START
echo ======================================================
echo.

:: 1. Xoa Git cu va Embedded Git
echo [1/4] Dang xoa bo lich su Git cu va Embedded Repos...
if exist ".git" rd /s /q ".git"
if exist "src\modules\dubbing\TMF_Local_Engine\MeloTTS-Vietnamese\.git" rd /s /q "src\modules\dubbing\TMF_Local_Engine\MeloTTS-Vietnamese\.git"
if exist "src\modules\dubbing\TMF_Local_Engine\MeloTTS_Vietnamese\.git" rd /s /q "src\modules\dubbing\TMF_Local_Engine\MeloTTS_Vietnamese\.git"
if exist "src\modules\dubbing\TMF_Local_Engine\XTTS-v2\.git" rd /s /q "src\modules\dubbing\TMF_Local_Engine\XTTS-v2\.git"
if exist "src\modules\dubbing\TMF_Local_Engine\espeak-ng\.git" rd /s /q "src\modules\dubbing\TMF_Local_Engine\espeak-ng\.git"

:: 2. Khoi tao Git moi
echo [2/4] Dang khoi tao Git moi...
git init
git branch -M main

:: 3. Ket noi va chuan bi
echo [3/4] Dang ket noi voi GitHub (MinhTriTM/IMO-AXON)...
git remote add origin https://github.com/MinhTriTM/IMO-AXON.git
echo (Vui long cho doi, dang nap hang nghin file du lieu ngon ngu...)
git add .
git commit -m "initial elite commit: MIMO-AXON modular ecosystem"

:: 4. Day code (Force Push)
echo [4/4] Dang day code len GitHub...
git push -u origin main --force

echo.
echo ======================================================
echo   DONE! GitHub da duoc lam sach va cap nhat hoan hao.
echo ======================================================
pause
