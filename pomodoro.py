 # Pomodoro Timer - Console Based
import time
import winsound
def beep():
    winsound.Beep(1000,500)
def countdown(minutes):
    seconds = int(minutes * 60)
    while seconds:
        mins = seconds // 60
        secs = seconds % 60
        print(f"{mins:02d}:{secs:02d}", end="\r")
        time.sleep(1)
        seconds -= 1
    beep() 
    print("00:00")
     
def pomodoro():
    study_time = 25 
    short_break = 5      
    long_break = 15       
    cycles = 4   

    for i in range(1, cycles + 1):
        print(f"\n➡ Cycle {i}: Study Time Started!")
        countdown(study_time)
        print("⏳ Study session complete!")

        if i != cycles:
            print("\n☕ Short Break!")
            countdown(short_break)
            print("🔔Short Break Over! Back To Study")
        else:
            print("\n🌿 Long Break!")
            countdown(long_break)
            print("🔔Long Break Over! Back To Study")

    print("\n🎉 All Pomodoro cycles completed!")
pomodoro()
