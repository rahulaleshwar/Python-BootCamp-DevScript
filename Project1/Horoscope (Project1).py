conditon = True
while conditon == True:
    print('''
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Zodiac signs~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Select a sign and your future will be predicted.Its all gone be fun!!!!!!!!!
        1.Aries	
        2.Taurus	
        3.Gemini	
        4.Cancer	
        5.Leo	
        6.Virgo	
        7.Libra	
        8.Scorpio	
        9.Sagittarius	
        10.Capricorn	
        11.Aquarius
        12.Pisces
      ''')

    z = int(input("Enter the zodiac number according to the list:"))
    if z == 1:
        print('''
        Aries:
        Limited capital will not prove an obstacle in putting a project on the road. Support of family members is assured in whatever you undertake. 
        Lucky Colour: Sky Blue Lucky Alphabet: J Friendly Numbers: 8, 16 Friendly Zodiac Today: Pisces & Virgo Be careful of: Libra''')
    elif z == 2:
        print('''
        Taurus:
         A new source of income is likely to open up and promises to make you financially secure. Fitness mantra of a friend will do wonders for your health. Happy time is foreseen at work as you tackle your job efficiently. 
         Lucky Colour: Purple Lucky Alphabet: D Friendly Numbers: 2, 4, Friendly Zodiac Today: Leo & Cancer Be careful of: Virgo''')
    elif z == 3:
        print('''
        Gemini:
        You will need to remain guarded, as you may be taken for a ride on the monetary front. Things that were going wrong on the work front will begin to improve. Those doing their bit to shed weight will succeed beyond their expectations!.
        Lucky Colour: Violet Lucky Alphabet: L Friendly Numbers: 6, 9 Friendly Zodiac Today: Scorpio & Leo Be careful of: Aries''')
    elif z == 4:
        print('''
        Cancer:
        You will benefit by taking a break from your regular exercise routine. Child or sibling may make you proud by his or her achievements. It will be prudent to keep a watchful eye on a business colleague. Your financial prudence will help keep the coffers brimming.
        Lucky Colour: Orange Lucky Alphabet: D Friendly Numbers: 1, 4, 7 Friendly Zodiac Today: Leo & Aries Be careful of: Scorpio''')
    elif z == 5:
        print('''
        Leo:
        A bad cold or some other small ailment may trouble on and off. A family member studying out of town or abroad may become a source of worry.
        Lucky Colour: Chocolate Lucky Alphabet: H Friendly Numbers: 6, 12 Friendly Zodiac Today: Taurus & Libra Be careful of: Gemini''')
    elif z == 6:
        print('''
        Virgo:
        An exciting time in a family gathering is foreseen. Avoid offending someone by your actions at work. Money well spent may give you inner satisfaction.
        Lucky Colour: Maroon Lucky Alphabet: D Friendly Numbers: 4, 9, 13 Friendly Zodiac Today: Scorpio & Sagittarius Be careful of: Cancer''')
    elif z == 7:
        print('''
        Libra:
        Your sympathetic touch will alleviate the problems of a family elder. Consistent performance will pave the way for promotion. Try not to overstep the budgeas.
        Lucky Colour: Lemon Lucky Alphabet: M Friendly Numbers: 3, 8, 11 Friendly Zodiac Today: Virgo & Scorpio Be careful of: Leo''')
    elif z == 8:
        print('''
        Scorpio:
        Getting your money back from someone may require efforts, but get back, you will! Less work will enable you to take some time off for yourself.
        Lucky Colour: Apricot LuckyAlphabet: K Friendly Numbers: 5, 9, 14 Friendly Zodiac Today: Aries & Scorpio Be careful of: Virgo''')
    elif z == 9:
        print('''
        Sagittarius:
        A property issue is likely to be resolved amicably. Performing well on the academic front will not pose much difficulty for you. Less work will enable you to take some time off for yourself.
        Lucky Colour: Brown Lucky Alphabet: S Friendly Numbers: 7, 14 Friendly Zodiac Today: Taurus & Leo Be careful of: Aries''')
    elif z == 10:
       print('''
       Capricorn:
        Something that is available on the house will help you save money. Some of you will have to adopt measures to blunt the impact of a lifestyle disease. Despite calling the shots, you may be made to toe the line in a professional situation.
        Lucky Colour: Violet Lucky Alphabet: G Friendly Numbers: 5, 10 Friendly Zodiac Today: Pisces & Libra Be careful of: Gemini''')
    elif z == 11:
        print('''
        Aquarius: 
        Speed and comfort is foreseen for those undertaking a long journey.
        Lucky Colour: Saffron Lucky Alphabet: P Friendly Numbers: 5, 7, 12 Friendly Zodiac Today: Cancer & Sagittarius Be careful of: Virgo''')
    elif z == 12:
        print('''
        Pisces:
        Watch your step on the financial front, as someone may sweet-talk you out of money.Visiting the site of your new home is possible. 
        Lucky Colour: Dark Turquoise Lucky Alphabet: N Friendly Numbers: 12, 16 Friendly Zodiac Today: Scorpio & Aries Be careful of: Taurus ''')
    else : print("Please enter the above numbers only!!!!!!!")
    
    conditon = True if input(" \n \n Do you want to try again? (Y/N): ") == 'Y' else print("~~~~~~~~~~~~THANKYOU~~~~~~~~~~~~~~~~~~~")
    

