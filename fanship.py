#let's explore naruto land hehehehhe , let's find out your fanship
anime=input("Do you like anime ")
if anime=="yes":
  print("oh!! so let's play this game ")
  naruto=input("Do you like Naruto: ")
  if naruto=="yes":
    print("great!!!! let's find out, are you a true fan or not")
    character=input("who is your favourite ")
    if character=="naruto":
      print("oh!!! ,,, answer this then ")
      Himyum=input("who was first person that accept naruto before hinta heheheheh !!!")
      if Himyum== "Ramen Ichiraku guy " or "Teuchi":
        print("congratulations  !!! bro , you rock bro ")
      else:
        print("sorry brother , but i know you are fan but don't worry ")
    elif character=="sasuke":
      print("okkk aayyy sasuke boy , your question to test your fanship")
      kiss=input("tell me his first kiss 😏😏😘😛")
      if kiss=="naruto":
        print("broooooo!!!!! sasuke loves you 🤣🤣🤣😘, you also deserve his kiss ")
      else:
        print("aahhhhhh no")
    elif character=="hinata":
      print("okay , princess lover , here for you ")
      first_love=input("name her first love")
      if first_love=="naruto":
        print("❤️❤️❤️, i was ready with her biyakugun to smash but 🤗🤗 but you pass")
      else:
        print("bye bye bye , why why , how can you do this 🥹🥹🥹🥹 go watch again ")
    elif character=="kakashi":
      print("Copy Ninja time! Let's see if you know him.")
      mask=input("What does Kakashi always wear on his face?")
      if mask.lower() == "mask":
        print("You are a true Kakashi fan! 😎")
      else:
        print("Nope! It's his mask. Go rewatch some episodes!")
    elif character=="sakura":
      print("Sakura fan! Let's test you.")
      crush=input("Who was Sakura's first crush?")
      if crush.lower() == "sasuke":
        print("Correct! You know her well 💗")
      else:
        print("Nope! It was Sasuke. Try again next time.")
    elif character=="itachi":
      print("Itachi lover, huh? Here's your question.")
      reason=input("Why did Itachi join Akatsuki?")
      if "protect" in reason.lower() or "sasuke" in reason.lower():
        print("You know the pain behind his eyes. Respect! 🙏")
      else:
        print("Not quite. He did it to protect Sasuke and the village.")
    else:
      print("Sorry, I don't have a question for that character yet!")
  else:
    print("No worries! There are many other great anime out there.")
else:
  print("Maybe give anime a try sometime!")