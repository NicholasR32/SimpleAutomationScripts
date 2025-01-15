; This script was written in AutoHotKey, and also has its own repo for some reason.

; AHK script that automatically buys enough upgrades and buildings to reach
; the required CpS, ascends, and then loops again in an Endless cycle.
#Requires AutoHotkey v2.0

; Press to terminate script at any time. Useful since you can't use the mouse
Backspace:: ExitApp

; Move mouse to the "Buy All Upgrades" button and click it.
; I consider this the "home" position for the cursor. All other mouse movement is relative to this position.
; This may change depending on your display setup and the position of your Cookie Clicker window.
; I had my game open and maximised on the second of two 1920 x 1080 monitors, so hence the x=3650.
Click 3650, 170

; Auto ascend however many times you want.
; You can make this whatever amount you need to get 1000 ascensions,
; or slightly less so you can do the last one yourself.
Loop 999
{
    ; Buy enough upgrades and buildings to gain prestige level.
    ; This can be 5 or even 4 rounds of buying, but with a 
    ; small risk of that ascension not counting. Your mileage may vary.
    Loop 6
    {
        ; Buy all upgrades.
        Loop 3
        {
            Click
            Sleep 50
        }

        ; Move left to collapse upgrade list.
        MouseMove -500, 0, 0, "R"
        Sleep 100

        ; Move to buy cursors.
        MouseMove 500, 130, 50, "R"

        ; Buy 100.
        Send "{Shift down}"
        Sleep 100

        ; Buy cursors.
        Loop 10
        {
            Click
            Sleep 50
        }

        ; Move down and buy grandmas.
        MouseMove 0, 100, 50, "R"
        Loop 10
        {
            Click
            Sleep 50
        }

        ; Move back up to Buy All Upgrades.
        Send "{Shift up}"
        MouseMove 0, -230, 50, "R"

        ; Wait briefly for new upgrades to appear.
        Sleep 500
    }

    ; Mouse should be on Buy All Upgrades at this point.

    ; Click Legacy button.
    MouseMove -160, -60, 50, "R"
    Click
    Sleep 100

    ; Ascend.
    Send "{Enter}"
    Sleep 100

    ; Cancel Big Cookie shattering animation.
    Send "{Esc}"

    ; Move back to Buy All Upgrades button.
    MouseMove 160, 60, 50, "R"
    Sleep 100

    ; Click Reincarnate button.
    MouseMove -777, -32, 50, "R"
    Click
    Sleep 100

    ; Confirm.
    Send "{Enter}"

    ; Move back to starting position.
    MouseMove 777, 32, 50, "R"

    ; Wait for everything to settle, then repeat.
    Sleep 3000
}