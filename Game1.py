import time

#this is my first project that is "big" if you could say so.

print("Welcome to my adventure game!\n")

name = input("What is your name?: ")
age = int(input("\nHow old are you? (you need to be atleast 12): "))

print("\nHello " + name + ",")

hp = int(100)

if age >= 12:
    print("You are old enough to play!\n")

    wants_to_play = input("Do you want to play?(yes or no): ").lower()
    if wants_to_play == "yes":
        print("\n\n\n\nLet's play!, you start with", hp ,"health/hp")



        left_or_right = input("\nYou see a two way path, one goes left, one goes right, which one do you choose?(left or right): ").lower()
        if left_or_right == "left":

            swim_or_around = input("\n\nYou followed the path... You see a big lake, you can swim or go around the lake. Which one do you choose?(swim or go around): ").lower()
            if swim_or_around == "swim":
                print("\n\nYou got dragged under the water by an unknown slimy object. You managed to escape but got hurt and lost 25 hp ")
                hp -= int(25)
                print("You have", hp ,"hp now.")

                stuck_in_the_lake = input("\n\nYou submerge to the surface to see no land anywhere, the water goes on for miles. You can swim or give up. (swim or give up):").lower()
                if stuck_in_the_lake == "swim":
                    print("\n\nYou got exhausted and the monster grabbed you under the water again, you don't have power to fight back. You lose.")
                    time.sleep(2)
                    print("\n\n\n\nYou got the Dead by tentacle ending")

                elif stuck_in_the_lake == "give up":
                    print("\n\nYou decided to just give up and float around, you fell asleep... ")
                    time.sleep(5)
                    boat_event = input("\n2 Hours later...\n\nYou wake up and hear a boat, you can shout or stay silent.(shout or silent): ").lower()

                else:
                    print("Invalid input.")

                    if boat_event == "shout":
                        print("\n\n\n\nThe people on the boat decided to shoot you. You lost.")
                        time.sleep(2)
                        print("You got the Dead by people on a ship ending")
                    else:
                        print("\n\nThe people on the boat decided to reel you onto the boat. After a long trip, you arrived to some kind of small town, the people in the town took you in their town. You decided to stay and live there.")
                        time.sleep(2)
                        print("\n\n\n\nYou got the real ending")



            else:
                run_or_staycalm = input("\n\nYou decide to walk around the lake, halfway around the lake, you see tentacles rise from the water, you can run into the forest or continue walking alongside with the beach.(run or continue): ").lower()

                if run_or_staycalm == "run":
                    print("you ran into the forest right next to you. You ran for quite the while because you got spooked")
                    time.sleep(2)
                    print("You dont know where to go, you keep wondering endlesly in the woods, you later lose your ability to do anything, it's like a magical force took over your body")
                    time.sleep(2)
                    print("\n\nYou got the infinite wonderer ending")

                elif run_or_staycalm == "continue":
                    print("\n\nYou decide to ignore the tentacles. You continued walking along side with the lake, about 5 minutes later, you got slapped by the tentacle and you flew to the ground, you lost 25 hp ")
                    hp -= int(25)
                    print("You now have", hp ,"hp")

                    print("\n\nYou get up a bit startled but continued walking\n\n")
                    time.sleep(5)
                    print("You arrive to your cottage and go inside. You continue your day like normal\n\n")
                    time.sleep(2)



                    go_fishing = input("\n\n\n\nYou think about going to fish, will you?(yes or no): ").lower()
                    if go_fishing == "yes":
                        print("You took your fishing rod and went fishing")
                        print("You are fishing without any worries, you catch few fish.\n\n\n\n\n\n")
                        time.sleep(5)


                        fight_or_no = input("After a while, suddenly a wolf bites your hand, will you fight it?(yes or no): ").lower()
                        if fight_or_no == "no":
                            print("\n\nYou died, why didn't you fight?\n\nYou lose")
                            time.sleep(2)
                            print("\n\n\n\nYou got the Dead by wolf ending")

                        elif fight_or_no == "yes":
                            print("\n\nYou managed to fight the wolf off, but you got badly injured and lost 74 hp!\n\n")
                            hp -= int(74)
                            print("You now have", hp ,"hp")

                            time.sleep(5)
                            print("You start running to your house in fear...")
                            time.sleep(5)
                            print("You fell and hit your head, you dont feel anything, you lose 5 hp")
                            hp -= int(5)
                            if hp <= 0:
                                time.sleep(5)
                                print("You died because your hp reached 0.\n\n")
                                print("You got the Dead by fall ending.")



                        else:
                            print("Invalid input.")

                    elif go_fishing == "no":
                        print("You are just sitting on a chair in your cottage, nothing changes, you leave your cottage after a few days and go home...")
                        time.sleep(2)
                        print("You got the Fake ending")

                    else:
                        print("Invalid input.")
                else:
                    print("Invalid input.")
        elif left_or_right == "right":
            print("\n\n\n\nYou fell into a wolfpit and got injured, you are now stuck. You lose...")
            time.sleep(2)
            print("You got the Stuck in a pit ending.")

        else:
            print("Invalid input.")

    elif wants_to_play == "no":
        print("\nOk, come back if you want to play")

    else:
        print("Invalid input.")

else:
    print("\nYou are not old enough to play")

#This is my first ever project that is bigger than couple lines of simple code.
#If you play this, thank you!
#You can leave comments to me, about what I should do better next time! I really want to learn more of coding!
