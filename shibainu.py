import pyautogui
pw = pyautogui.password(text="Please enter your quiz's password before playing.", title="Quiz game by Austiniverse")
if pw == "np4u":
    pw = pyautogui.confirm(text="choose 1", title="nopassword4u", buttons=["canisleepwithyou", "ryzermattishandsome", "lattecookiezaredelicious"])
if pw == "canisleepwithyou":
    pw = pyautogui.confirm(text="can i sleep with you", title="Question 1", buttons=["yes babe", "no you fucking idiot get outta my face"])
    if pw == "yes babe":
        pyautogui.alert(text="no.", title="answer to that question")
    else:
        pyautogui.alert(text="ok good", title="Answer of Question 1")
        pw = pyautogui.prompt(text = "1 + 1 = ?", title="Question 2 (extremely hard math question)", default = "-->  69420 <--")
        pyautogui.confirm(text = "you're so good ok u passed the test lets goo", title='dababy', buttons=["ok sir i know im good"])
        pw = pyautogui.confirm(text="Can Infinity Power exist?", title="Question 3", buttons=["yes :)", "no >:("])
        if pw == "yes :)":
            pyautogui.confirm(text="Ok, it's actually true.", title="answer", buttons=["wait r u wrong"])
            pyautogui.confirm(text="oh yes", title="xd", buttons=["exit"])
        else:
            pyautogui.confirm(text = "ur soooo good", title = "omg howowowowowo", buttons=['end test'])
            pyautogui.alert(text="can u tell austin that u completed the test and send him a screenshot?", title="help")
if pw == "ryzermattishandsome":
    pw = pyautogui.confirm(text = "are you sure that he's handsome?", title="r u sure?", buttons=["yes", "no"])
    if pw == "no":
        pyautogui.alert(text = "You said that HE IS NOT HANDSOME? GET OUTTA MY FACE RIGHT NOW", title=">:(")
    else:
        pyautogui.alert(text="great job! u passed the test",title="microsoft winwos xp")
        naem = pyautogui.prompt(text = "please enter your name", title="name assign")
        pyautogui.confirm(text = "welcome to the test, " + naem +" my friend.", title="Welcome.")
        pw = pyautogui.confirm(text="1+1/2 is ...", title="certified math question", buttons=["0.69", "69","1.5", "0.05", "0.5", "0.7", "2.7"])
        if pw == "1.5":
            pyautogui.alert(title="good job", text="u r sooo good")
            pw = pyautogui.confirm("Congrats! You have done the test, "+ naem + ".", buttons=["quit", "show me how do i proof austin that i completed the test"])
            if pw == 'show me how do i proof austin that i completed the test':
                pyautogui.confirm(text = "u should screenshot the next window after you press ok", title="how", buttons=["OK"])
                pyautogui.confirm(text="ayo austin i, "+ naem + " completed the test that u cant complete LMFAO", title="austin u suck", buttons=["YOU SUCK AUSTIN"])
        else:
            pyautogui.alert(text="u r sooo bad lmao", title="bad math kid")
if pw == "lattecookiezaredelicious":
    pyautogui.alert(text="work in progress")