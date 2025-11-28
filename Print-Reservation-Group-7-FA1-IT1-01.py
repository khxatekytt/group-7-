import os
class userinfo:
    def __init__(self, name, pword):
        self.username = name
        self.password = pword
        self.requests = [] 
        self.requestamount = 0
        self.rejects = 0
    def requestqueue(self):
        name = input(" Input file name:\n >> ")
        date = input(" Input date to receive:(MM/DD/YYYY format)\n >> ")
        self.requests.append([name, date, "NOT APPROVED YET", " "])
        self.requestamount += 1
    def displayall(self, adminstatus):
        count = 0
        print(f" Username: {self.username}")
        while count < self.requestamount:
            print(f" - Queue {(count + 1)}\n - File name: {self.requests[count][0]}\n - Date {self.requests[count][1]}\n Status: {self.requests[count][2]}")
            if adminstatus == 1:
                if self.requests[count][2] == "REJECTED":
                    print(f" Reason: {self.requests[count][3]}")
            count += 1
    def adminapprove(self, index):
        if self.requests[index][2] == "APPROVED":
            input(" Reqeust has already been approved.\n Press Enter key to continue...")
        else:
            self.requests[index][2] = "APPROVED"
            input(" Request approved. Press Enter key to continue...")
    def adminreject(self, index):
        if self.requests[index][2] == "REJECTED":
            input(" Request has already been rejected.\n Press Enter key to continue...")
        else:
            self.requests[index][2] = "REJECTED"
            self.requests[index][3] = input(" Enter reason:\n >> ")
            self.rejects += 1
            input(" Request rejected. Press Enter key to continue...")
users = []
usercount = 0
inp = 0
while(True):
    os.system('cls')
    inp = input("\n Welcome to Four Angel Copy Print online printing services.\n [1] Sign in\n [2] Sign Up\n [3] Exit\n >> ")
    if inp == '1':
        os.system('cls')
        userinput = input(" Enter Username: ")
        passinput = input(" Enter Password: ")
        i = 0
        if userinput == "admin" and passinput == "testpass":
            j, tempcount = 0, 0
            while j < len(users):
                tempcount = tempcount + (int(users[j].requestamount) - int(users[j].rejects))
                j += 1
            while (True):
                os.system('cls')
                choice = input(f"\n Welcome Admin\n You have [{tempcount}] approved/unapproved/rejected printing requests!\n [1] View all requests\n [2] Approve/Reject requests\n [3] Sign out\n >> ")
                if choice == '1':
                    j = 0
                    if usercount > 0 and tempcount > 0:
                        while j < usercount:
                            users[j].displayall(0)
                            j += 1
                    else: print("\n Your reservation list is empty.")
                    input("\n Press Enter key to continue...")
                elif choice == '2':
                    j, k = 0, 0
                    if usercount > 0 and tempcount > 0:
                        while (tempcount > 0):
                            os.system('cls')
                            temp = int(users[j].requestamount)
                            print(f"User: {users[j].username}\n - File name: {users[j].requests[k][0]}\n - Date: {users[j].requests[k][1]}\n Status: {users[j].requests[k][2]}")
                            choice = input(" [1] Previous\n [2] Next\n [3] Approve request\n [4] Reject request\n [5] End\n >> ")
                            if choice == '1':
                                if j == 0 and k == 0:
                                    input(" You are at the start of the list.\n Press Enter key to continue...")
                                elif j > 0 and k == 0:
                                    j -= 1
                                    k = (temp - 1)
                                else: k -= 1
                            elif choice == '2':
                                if j == (usercount - 1) and k == (temp - 1):
                                    input(" You are at the end of the list.\n Press Enter key to continue...")
                                elif j < usercount and k == temp - 1:
                                    j += 1
                                    k = 0
                                else: k += 1
                            elif choice == '3':
                                users[j].adminapprove(k)
                            elif choice == '4':
                                users[j].adminreject(k)
                            elif choice == '5': break
                            else:   input(" Your input is invalid. Please try again.\n Press Enter to continue...")
                    else: input("\n Your reservation list is empty.\n Press Enter key to continue...")
                elif choice == '3': break
                else: input(" Your input is invalid. Please try again.\n Press Enter to continue...")
        elif usercount == 0: input("\n User does not exist.\n Press Enter to continue...")
        else:
            while i < len(users):
                if users[i].username == userinput and users[i].password == passinput:
                    while (True):
                        os.system('cls')
                        test = input(f" Welcome! {users[i].username}\n [1] Queue new print reservation\n [2] View request(s) status\n [3] Delete request(s)\n [4] Sign out\n >> ")
                        if test == '1':
                            users[i].requestqueue()
                            input(" Request queue succesfully added!\n Press Enter to continue...")
                        elif test == '2':
                            print(f"\n You currently have: \n - {users[i].requestamount} reservations")
                            if users[i].rejects > 0:
                                print(f" - {users[i].rejects} rejected reservations")
                            if users[i].requestamount > 0:
                                test = input("\n View details? \n [1] Yes\n [2] No\n >> ")
                                if test == '1':
                                    users[i].displayall(1)
                                    input("\n Press Enter key to continue...")
                            else: input("\n You have no reservations.\n Press Enter key to continue...")
                        elif test == '3':
                            j = 0
                            if users[i].requestamount == 0:
                                input("\n You have no reservations.\n Press Enter key to continue...")
                            else:
                                while (users[i]. requestamount > 0):
                                    os.system('cls')
                                    temp = users[i].requestamount
                                    if users[i].requestamount > 0:
                                        print(f"User: {users[i].username}\n - File name: {users[i].requests[j][0]}\n - Date: {users[i].requests[j][1]}\n Status: {users[i].requests[j][2]}")
                                        choice = str(input(" [1] Previous\n [2] Next\n [3] Delete request\n [4] End\n >> "))
                                        if choice == '1':
                                            if j == 0: input("\n You are at the start of the list.\n Press Enter key to continue...")
                                            else: j -= 1
                                        elif choice == '2':
                                            if j == (temp - 1): input("\n You are at the end of the list.\n Press Enter key to continue...")
                                            else: j += 1
                                        elif choice == '3':
                                            del users[i].requests[j]
                                            users[i].requestamount -= 1
                                            users[i].rejects -= 1
                                            input("\n Request successfully deleted.\n Press Enter key to ccontinue...")
                                            break
                                        elif choice == '4': break
                                        else: input("\n Your input is invalid. Please try again.\n Press Enter to continue...")
                                    else:
                                        input("\n You have no more reservations.\n Press Enter key to continue...")
                                        break
                        elif test == '4':
                            input(" Thank you for using the reservation service.\n Press Enter to continue...")
                            break
                        else:
                            input(" Your input is invalid. Please try again.\n Press Enter to continue...")
                            continue
                if i == usercount:
                    input("\n User does not exist.\n Press Enter to continue...")
                i += 1
    elif inp == '2':
        newuser = "user" + str(usercount)
        users.append(newuser)
        while (True):
            os.system('cls')
            i = 0
            name = input(" Enter Username: ")
            password = input(" Enter New Password: ")
            confirmpass = input(" Confirm Password: ")
            if usercount > 0:
                while (i < usercount):
                    if users[i].username == name: input("\n Username already exists. Please input another one. \n Press Enter to continue...")
                    i += 1
            if confirmpass != password:
                input("\n Your passwords does not match. \n Press Enter to continue...")
            else:
                input("\n Account successfully created! \n Press Enter to continue...")
                break
        users[usercount] = userinfo(name, password)
        usercount += 1
    elif inp == '3':
        os.system('cls')
        input("\n Exiting program.\n Press Enter key to continue...")
        break
    else:
       input(" Your input is invalid. Please try again.\n Press Enter to continue...")
