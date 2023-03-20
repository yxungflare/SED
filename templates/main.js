const {app, BrowserWindow} = require('electron');
const { spawn } = require('child_process');

let flaskProcess = null

    
function createWindow() {
    const win = new BrowserWindow({
        width: 1600,
        height: 900,
        icon:"img/i.png",
        autoHideMenuBar: true,
        resizable: false,
        webPreferences:{
            nodeIntegration: true
        }
    });

    win.loadFile('page2.html');
    flaskProcess = spawn('python', ['etc\py\page3.py'])
}

app.whenReady().then(createWindow);

app.on('window-all-closed', () => {
    if(process.platform !== 'darwin')
    {
        
        // Останавливаем Flask-приложение
        flaskProcess.kill()
        flaskProcess = null
        app.quit();
    }
});

app.on('activate', () => {
    if(BrowserWindow.getAllWindows().length ===0){
        createWindow();
    }
});