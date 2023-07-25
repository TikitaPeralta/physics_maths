print("Hi! This is a lesson on Vectors :)")


while True:

    scalar_q = input("First off, how would you describe a scalar? ").lower()

    if scalar_q == "magnitude" or scalar_q == "number" or scalar_q == "length":
            print("absolutely right!")

            while True:
                vector_q = input("So, how would you describe a vector? ").lower()
                if vector_q == "magnitude and direction" or vector_q == "arrow" or vector_q == "size and direction":
                    print("yes!")
                    print("this chapter contains examples of vectors and explanations of the geometry side of it all... have fun exploring!")
                    break
                else:
                    print("try again!")
                    continue
            break
    else:
        print("try again!")
        continue