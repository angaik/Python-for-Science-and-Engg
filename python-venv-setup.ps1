function Add-Python-Venv {
    param (
        $venv_name
    )
    
    $python_path = "E:\Python\pyver\py3913\python.exe"

    & $python_path -m venv $venv_name
}

# Run within venv's directory
function Add-BasicPythonPkgs {
    Copy-Item "E:\Python\requirements\requirements_without_versions.txt"

    .\Scripts\Activate.ps1

    pip install -r requirements_without_versions.txt
    python -m pip install --upgrade pip
}