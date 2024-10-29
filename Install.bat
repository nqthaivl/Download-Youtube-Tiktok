@echo off
SETLOCAL ENABLEDELAYEDEXPANSION

REM Kiem tra xem Python da duoc cai dat chua
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Python chua duoc cai dat. Dang tai xuong Python...
    
    REM Tai xuong Python (thay doi phien ban neu can)
    curl -o python-installer.exe https://www.python.org/ftp/python/3.10.0/python-3.10.0-amd64.exe
    
    REM Cai dat Python
    start /wait python-installer.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0
    
    REM Xoa file cai dat
    del python-installer.exe
    
    echo Python da duoc cai dat thanh cong.
) ELSE (
    echo Python da duoc cai dat.
)

REM Kiem tra xem pip da duoc cai dat chua
pip --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo pip chua duoc cai dat. Dang cai dat pip...
    
    REM Cai dat pip
    curl -o get-pip.py https://bootstrap.pypa.io/get-pip.py
    python get-pip.py
    
    REM Xoa file cai dat
    del get-pip.py
    
    echo pip da duoc cai dat thanh cong.
) ELSE (
    echo pip da duoc cai dat.
)

REM Kiem tra cac thu vien trong requirements.txt
IF EXIST requirements.txt (
    echo Dang kiem tra cac thu vien trong requirements.txt...
    for /f "delims=" %%i in (requirements.txt) do (
        pip show %%i >nul 2>&1
        IF ERRORLEVEL 1 (
            echo Thuvien %%i chua duoc cai dat. Dang cai dat...
            pip install %%i
        ) ELSE (
            echo Thuvien %%i da duoc cai dat.
        )
    )
    echo Tat ca cac thu vien da duoc kiem tra va cai dat.
) ELSE (
    echo Khong tim thay file requirements.txt. Vui long tao file nay truoc khi chay script.
)

REM Kiem tra xem file Download Video.py co ton tai khong
IF EXIST "Download.py" (
    echo Dang chay file Download Video.py...
    python "Download.py"
) ELSE (
    echo Khong tim thay file Download.py. Vui long kiem tra lai.
)

ENDLOCAL
pause
