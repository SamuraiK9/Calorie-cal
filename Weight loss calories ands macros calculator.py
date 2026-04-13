#weight loss calorie and macros calculator

#input in kg or lbs


def main():
    print("Hello welcome to your weight loss calculator, we will workout your caloric intake and macros to reach your goal bodyweight")

    while True:
        user_pref = input("If you would like to proceed in pounds then type 'lbs' or if in kilograms then type 'kg': ").lower()

        if user_pref == "lbs":
            lbs()
            break
        
        elif user_pref == "kg":
            kg()
            break
              
        else:
            print("You must enter a valid response")
            continue
       

       
def lbs():
    goal_bw_lbs = input("What bodyweight do you want to get to?. Type in numeric only: ").strip()
    if goal_bw_lbs.isdigit():
        goal_bw_lbs = int(goal_bw_lbs)
    else:
        raise ValueError("Type in numeric only")

    total_daily_cal = goal_bw_lbs * 12 #formula for goal body weight; weight in lbs x 12
    protein = goal_bw_lbs #1g of protein per lb of bodyweight
    fat_in_lbs = total_daily_cal * 0.25 #25% of calries fat
    fat = round(fat_in_lbs / 9, 1)
    carbs_in_lbs = total_daily_cal - protein - fat_in_lbs #remainder is carbs
    carbs = round(carbs_in_lbs / 4, 1)
#to get g every 1g of fat is = 9cal and every 1g of carbs = 4cal
    print(f"Your total daily calories should be {total_daily_cal}")
    print(f"Your macros should be: Protein: {protein}g, Fat: {fat}g and Carbohydrates: {carbs}g per day")
    print("Remember that your carbohydrates should be healthy ones mostly and not too starchy and try to keep your fats more unsaturated. GOOD LUCK!!")

def kg():
    goal_bw_kgs = input("What bodyweight do you want to get to?. Type in numeric only: ").strip()
    if goal_bw_kgs.isdigit():
        goal_bw_kgs = int(goal_bw_kgs)
    else:
        raise ValueError("Type in numeric only") 

    #1kg is equal to 2.20462lb
    goal_bw_lbs = round(goal_bw_kgs * 2.220462, 1) 
    total_daily_cal = round(goal_bw_lbs * 12, 0)
    protein = goal_bw_lbs 
    fat = round((total_daily_cal * 0.25) / 9, 1)
    carbs = round(((total_daily_cal - protein) - (total_daily_cal * 0.25)) / 4, 1) #remainder is carbs
    
    #to get g every 1g of fat is = 9cal and every 1g of carbs = 4cal
    print(f"Your total daily calories should be {total_daily_cal}")
    print(f"Your macros should be: Protein: {protein}g, Fat: {fat}g and Carbohydrates: {carbs}g per day")
    print("Remember that your carbohydrates should be healthy ones mostly and not too starchy and try to keep your fats more unsaturated. GOOD LUCK!!")


if __name__ == "__main__":
    main()
