def caffe(beverage, *arguments, **keywords):
    print("Do U have any", beverage, "?")
    for arg in arguments:
        print(arg)
    print("*****")
    for kw in keywords:
        print(kw, ":", keywords[kw])

caffe("coffee", "it's yummy, sir.", "Wolud you try?",
      barista = "Jay Kim",
      client = "BSSM",
      cup = "Venti-size")