def span_comp(self):

        print("Welcome\n")
        print("Starting up...\n")
        time.sleep(1)


        while True:
                time.sleep(1)
                print("\nFunctions:")
                print("1. Today's Word")
                print("2. Yesterday's Word")
                print("3. Words the last week")
                print("4. Words the last month")
                print("5. Words the last year")
                print("6. Quiz")
                print("7. Hiscores - Top Points")
                print("8. Hiscores - Highest Correction %")
                print("9. Hiscores - Most Questions")
                print("10. Exit")
                print("\n")
                time.sleep(1)
                choice = int(input("Which function would you like to use? 1/2/3/4/5/6/7/8/9/10: "))
                print("\n")



                if choice == 1:
                    print("\nLoading...\n")
                    time.sleep(1)
                    Spanish.today(" ")
                    time.sleep(1)

                elif choice == 2:
                    print("\nLoading...\n")
                    time.sleep(1)
                    Spanish.yesterday(" ")
                    time.sleep(1)

                elif choice == 3:
                    print("\nLoading...\n")
                    time.sleep(1)
                    Spanish.week(" ")
                    time.sleep(1)

                elif choice == 4:
                    print("\nLoading...\n")
                    time.sleep(1)
                    Spanish.month(" ")
                    time.sleep(1)

                elif choice == 5:
                    print("\nLoading...\n")
                    time.sleep(1)
                    Spanish.year(" ")
                    time.sleep(1)
                    
                elif choice == 6:
                    print("\nLoading...\n")
                    time.sleep(1)
                    Spanish.Quiz(" ")
                    time.sleep(1)
                    
                elif choice == 7:
                    print("\nLoading...\n")
                    time.sleep(1)
                    Spanish.top_points(" ")
                    time.sleep(1)

                elif choice == 8:
                    print("\nLoading...\n")
                    time.sleep(1)
                    Spanish.top_percent(" ")
                    time.sleep(1)
                    
                elif choice == 9:
                    print("\nLoading...\n")
                    time.sleep(1)
                    Spanish.top_questions(" ")
                    time.sleep(1)
                    
                
                elif choice == 10:
                    print("Shutting down...\n")
                    time.sleep(1)
                    print('Gracias!')
                    time.sleep(1)
                    break


                else:
                    print("Not a valid input")    