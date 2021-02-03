import os, yaml, sys

def main():
    args = (sys.argv)
    del list[0]

    
    branch = ""
    print(list)
    for b in list:
        if "releases" in b:
            branch = b
            break
    
    if branch == "":
        print("develop")
    else:
        branch_list = branch.split("/")
        if branch_list[-2] == "releases":
            print(branch_list[-2]+"/"+branch_list[-1])
        else:
            print("develop")
    

if __name__ == "__main__":
    main()
