SetTitleMatchMode, 2  ; Match substring anywhere in the window title

; Try to toggle Play/Pause for Spotify

; Kodi
IfWinExist, Kodi
{
    WinActivate
    Send {Media_Play_Pause}
    ExitApp
}

; VLC
IfWinExist, VLC 
{
    WinActivate
    Send {Media_Play_Pause}
    ExitApp
}

IfWinExist, Spotify
{
    WinActivate
    Send {Media_Play_Pause}
    ExitApp
}

; Brave
IfWinExist, Brave
{
    WinActivate
    Send {Media_Play_Pause}
    ExitApp
}

; Google Chrome
IfWinExist, Chrome
{
    WinActivate
    Send {Media_Play_Pause}
    ExitApp
}

; Fallback
ExitApp