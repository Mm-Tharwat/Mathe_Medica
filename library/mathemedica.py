# -------------------------------------- Mathematical Functions ----------------------------------------

#(fun_1) check palindrome 
def palindrome(your_str):
    pal_s=""
    for i in your_str:
        pal_s=i+pal_s
    if your_str==pal_s:
        return f"{your_str} is palindrome "
    else:
        return f"{your_str} isn't palindrome as its reverse is {" "}{pal_s}"

#(fun_2) calculate npr "permutations"
def nPr(n,r):
    def factt(x):
        fact_x=1
        for i in range(1,x+1):
            fact_x*=i
        return fact_x
    if n<r:
        return "error!!! n must be >= r"
    else:
        npr=int( factt(n)/factt(n-r))
        return npr

#(fun_3) calculate ncr "combinations"
def nCr(n,r):
    def factt(num):
        fact_num=1
        for i in range (1,num+1):
            fact_num*=i
        return fact_num
    if n<r:
        return "error!!! must be > r "
    else:
        ncr= int((factt(n)/(factt(r)*factt(n-r))))
        return ncr

#(fun_4) print divisors of a num
def divisors(num):
    num_divisors=[]
    for i in range(1,num+1):
        if num%i==0:
            num_divisors.append(i)
    return num_divisors

#(fun_5) find GCD " greatest common divisor"
def GCD(num1,num2):
    while num1 != num2:
        if num1 > num2:
            num1-=num2
        else:
            num2-=num1
    return num1

#(fun_6) print fibonacci series
def fibonacci(num):
    def fibonacci(num):
        if num<=0:
            return 0
        elif num==1:
            return 1
        else:
            return fibonacci(num-1)+fibonacci(num-2)
    for i in range(num):
        print(fibonacci(i),end=" ")

#(fun_7) print fibonacci series reversed
def rev_fibonacci(num):
    a,b=0,1
    fibo_ser=[]
    for i in range(num):
        fibo_ser.append(a)
        a,b=b,a+b
        rev_ser=fibo_ser[::-1]
    for j in rev_ser:
        print(j,end=" ")
        
#(fun_8) find mean of numbers
def mean(ls): 
    sum=0
    for j in ls:
        sum+=j
    mean= sum/len(ls)
    return mean

#(fun_9) find medium of numbers
def medium(ls): 
    for j in range(len(ls)):
        for k in range(j+1,len(ls)):
            if ls[j]>ls[k]:
                ls[j],ls[k]=ls[k],ls[j]
    if len(ls)%2!=0:
        medium=ls[int((len(ls)+1)/2)-1]
        return medium
    else:
        medium=(ls[int((len(ls)/2)+1)-1]+ls[int((len(ls)/2))-1])/2
        return medium

#(fun_10) find mode of set of numbers
def mode(ls):
    most_repeat=0
    max_count=0
    for i in ls:
        count=0
        for j in ls:
            if i==j:
                count+=1
        if count>max_count:
            max_count=count
            most_repeat=i
    return most_repeat

#(fun_11) print pascal triangle
def pascal(number_of_rows): 
    for i in range(number_of_rows):
        num=1
        print(" "*(number_of_rows-i-1),end=" ")
        for j in range(i+1):
            print(int(num),end=" ")
            num= num*((i-j)/(j+1))
        print()

#(fun_12) print reversed pascal
def rev_pascal(number_of_rows):
    for i in range(number_of_rows):
        for j in range(i):
            print(" "*(i-number_of_rows),end=" ")
        num=1
        for j in range(number_of_rows-i):
            print(num,end=" ")
            num=num*(number_of_rows-i-j-1)//(j+1)
        print()

#(fun_13) calculate sum of two matrix
def sum_matrices(matrix1,matrix2):
    if len(matrix1)!=len(matrix2) or len(matrix1[0])!=len(matrix2[0]):
        return ["NOT Same Dimensions"]
    result=[]
    x=[]
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            x.append(matrix1[i][j]+matrix2[i][j])
    result.append(x)
    return result

#(fun_14) subtract two matrix
def subtract_matrices(matrix1,matrix2):
    if len(matrix1)!=len(matrix2) or len(matrix1[0])!=len(matrix2[0]):
        return ["NOT Same Dimensions"]
    result=[]
    x=[]
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            x.append(matrix1[i][j]-matrix2[i][j])
    result.append(x)
    return result

#(fun_15) times two matrix
def times_matrices(matrix1,matrix2):
    if len(matrix1[0])!=len(matrix2):
        return ["number of columns of first matrix not equal number of rows second matrix "]
    result=[[0 for num in range(len(matrix2[0]))]for num2 in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j]+=matrix1[i][k]*matrix2[k][j]
    return result

#(fun_16) check prime number
def is_prime(num):
    if num==2:
        return True
    if num>1:
        for j in range(2,int(num**0.5)+1):
            if num%j==0:
                return False
        else:
            return True

#(fun-17) calculate area of chosen figure
def area(figure,*parameter):
    if figure=="square":
        l=parameter
        return l**2
    elif figure=="rectangle":
        l,w=parameter
        return l*w
    elif figure=="circle":
        pi,r=parameter
        return pi*r**2
    elif figure=="triangle":
        base,height=parameter
        return 0.5*base*height
    elif figure==" sphere":
        pi,r=parameter
        return 4*pi*r**2
    elif figure=="trapezium":
        base1,base2,h=parameter
        return 0.5*(base1+base2)*h
    elif figure=="sector":
        r,length_of_arc=parameter
        return 0.5*r*length_of_arc
    elif figure=="rhombus":
        side_length,height=parameter
        return side_length*height
    elif figure=="parallelogram":
        any_base,its_height=parameter
        return any_base*its_height
    elif figure=="cube":
        side_length=parameter
        return 6*side_length**2
    elif figure==" cuboid":
        length,width,height=parameter
        return 2*(length*height+length*width+width*height)
    elif figure=="cone":
        pi,radius,length=parameter
        return (pi*radius*length)+(pi*radius**2)
    elif figure=="cylinder":
        pi,radius,height=parameter
        return 2*pi*radius*(height+radius)

#(fun_18) calculate volume of chosen figure
def volume(figure,*parameters):
    if figure=="cube":
        side_length=parameters
        return side_length**3
    elif figure=="cuboid":
        length,width,height=parameters
        return length*width*height
    elif figure=="sphere":
        pi,radius=parameters
        return (4/3)*pi*radius**3
    elif figure=="cone":
        pi,radius,height=parameters
        return (1/3)*pi*(radius**2)*height
    elif figure=="prism":
        area_of_base,height=parameters
        return area_of_base*height
    elif figure=="pyramid":
        area_of_base,height=parameters
        return (1/3)*area_of_base*height
    elif figure=="cylinder":
        pi,radius,height=parameters
        return pi*height*radius**2

#(fun_19) check number is armstrong or not
def is_armstrong(number):
    x=str(number)
    power=len(x)
    result=0
    for i in x:
        result+=int(i)**power
        if result==number:
            return True
    else:
        return False

#(fun_20) check number is a perfect number or not
def is_perfect_number(number):
    num_divisors=[]
    for i in range(1,number):
        if number%i==0:
            num_divisors.append(i)
    result=0
    for j in num_divisors:
        result+=j
        if number==result:
            return True
    else:
        return False


# -------------------------------------- Medical Functions ----------------------------------------

#(fun_1) BMI
def BMI(weight,height):
    bmi=weight/(height**2) 
    if bmi<16:
        return f"bmi equal {bmi} and category is Severe thinness"
    elif 16<=bmi<17:
        return f"bmi equal {bmi} and category is Moderate"
    elif 17<=bmi<18.5:
        return f"bmi equal {bmi} and category is Mild"
    elif 18.5<=bmi<25:
        return f"bmi equal {bmi} and category is Normal weight"
    elif 25<=bmi<30:
        return f"bmi equal {bmi} and category is pre_obesity" 
    elif 30<=bmi<35:
        return f"bmi equal {bmi} and category is obesity class I"   
    elif 35<=bmi<40:
        return f"bmi equal {bmi} and category is obesity class II" 
    else:
        return f"bmi equal {bmi} and category is obesity class III"  

#(fun_2) track glucose level
def track_glucose(glucose_level,is_fasting=True):
    if is_fasting:
        if glucose_level<70:
            return "low blood sugar, please eat something sweet"
        elif 70<=glucose_level<=99:
            return "normal fasting blood sugar"
        elif 100<=glucose_level<=125:
            return "prediabetes(impaired fasting glucose)"
        else:
            return "high blood sugar (Diabetes)"
    else:
        if glucose_level<70:
            return "low blood sugar, please eat something sweet"
        elif glucose_level<140:
            return "normal blood sugar"
        elif 140<=glucose_level<=199:
            return " prediabetes (Impaired glucose tolerance)"
        else:
            return "high blood sugar (Diabetes)"

#(fun_3) check blood pressure
def check_blood_pressure(systolic,diastolic):
    if systolic<90 or diastolic<60:
        return "low blood pressure"
    elif 90<=systolic<=120 and 60<=diastolic<=80:
        return "normal blood pressure"
    elif 120<systolic<=129 and diastolic<80:
        return " Elevated blood pressure"
    elif 130<=systolic<=139 or 80<=diastolic<=89:
        return "Hypertension stage 1"
    elif 140<=systolic<=180 or 90<=diastolic<=120:
        return "Hypertension stage 2"
    elif systolic>180 or diastolic>120:
        return "seek medical attention immediately,  its hypertensive crisis"
    else:
        return "blood pressure reading is unclassified"

#(fun_4) check oxygen level 
def check_oxygen_level(oxygen_level):
    if oxygen_level<90:
        return "Severe hypoxemia , please seek medical attention immediately"
    elif 90<=oxygen_level<=94:
        return "oxygen level is slightly low "
    elif 95<=oxygen_level<=100:
        return " normal oxygen level"
    else:
        return " Invalid value as oxygen level can't exceed 100%"

#(fun_5) cholesterol level analysis
def cholesterol_level_analysis(total_cholesterol,ldl,hdl):
    if total_cholesterol<200 and ldl<100 and hdl>=60:
        return "Excellent cholesterol level"
    elif total_cholesterol<200 and ldl<100 and hdl>=40:
        return "Healthy cholesterol level..you should make healthy diet and exercise "
    elif 200<=total_cholesterol<=239 or 130<=ldl<=159:
        return "Border line high cholesterol"
    elif total_cholesterol>=240 or ldl>=160:
        return "High cholesterol please see a doctor"
    elif hdl<40:
        return """Low HDL cholesterol.
        this may increase your risk for heart disease so you should improving your HDL through exercise and healthy fat"""
    else:
        return "unclassified cholesterol level"

#(fun_6) check protein level 
def check_protein_level(total_protein):
    if total_protein<6:
        return "Low protein level (Hypoproteinemia) and it possible causes liver disease "
    elif 6<=total_protein<=8.3:
        return "Normal protein level"
    elif total_protein>8.3:
        return "High protein level(Hyperprotrinemia) and it possible causes dehydration"
    else:
        return "Invalid value "

#(fun_7) check sleep quality
def sleep_quality(sleeping_hours,deep_sleep_percentage):
    if sleep_quality<6 or deep_sleep_percentage<15:
        return "Poor sleep quality"
    elif 6<=sleeping_hours<7 and 15<=deep_sleep_percentage<20:
        return "fair sleep quality"
    elif 7<=sleeping_hours<=9 and deep_sleep_percentage>=20:
        return "Good sleep quality"

#(fun_8) amount of caffeine allowed during day
def caffeine_amount(weight,age):
    if age<12:
        return "caffeine intake isn't individuals under 12 years old"
    elif 12<=age<18:
        max_amount= weight*2.5
        return f" Recommended maximum caffeine amount for teenagers is: {max_amount} mg/day"
    elif age>=18:
        return "Recommended maximum caffeine amount for adults is 400 mg/day"

#(fun_9) calculate and check body fat percentage 
def body_fat_percentage(weight,height,age,gender):
    bmi= weight/(height**2)
    if gender=="male":
        body_fat=((1.20*bmi)+(0.23*age))-16.2
    elif gender=="female":
        body_fat=((1.20*bmi)+(0.23*age))-5.4
    body_fat= (int(body_fat*100)/100)
    if gender=="male":
        if body_fat<6:
            result="low fat percentage (underfat)"
        elif 6<=body_fat<=24:
            result="normal fat percentage"
        else:
            result="high fat percentage(overfat)"
    elif gender=="female":
        if body_fat<14:
            result="low fat percentage (underfat)"
        elif 14<=body_fat<=31:
            result="normal fat percentage"
        else:
            result="high fat percentage(overfat)"
    return f" body fat percentage:{body_fat}% ,{result}"

#(fun_10) check heart health
def heart_health_check(daily_activity_hours,cholesterol_level,systolic_bodypressure,diastolic_bodypressure):
    if daily_activity_hours<0.5:
        activity_rate="low activity"
    elif 0.5<=daily_activity_hours<=2:
        activity_rate="Moderate activity"
    else:
        activity_rate="high activity"
    if cholesterol_level<200:
        cholesterol_rate="healthy cholesterol level"
    elif 200<=cholesterol_level<=239:
        cholesterol_rate="Border line high cholesterol"
    else:
        cholesterol_rate=" high cholesterol"
    if systolic_bodypressure<120 and diastolic_bodypressure<80:
        bodypressure_rate="normal blood pressure"
    elif 120<=systolic_bodypressure<=139 or 80<=diastolic_bodypressure<=89:
        bodypressure_rate="prehypertension"
    else:
        bodypressure_rate="hypertension"
    if activity_rate=="high activity" and cholesterol_rate=="healthy cholesterol level" and bodypressure_rate=="normal blood pressure":
        health_rate="Good heart health"
    elif cholesterol_rate==" high cholesterol" or bodypressure_rate=="hypertension":
        health_rate="poor heart health ,consider a healthy lifestyle"
    else:
        health_rate="Moderate heart health, you need some lifestyle adjustments"
    return f"Activity:{activity_rate},cholesterol:{cholesterol_rate},blood pressure:{bodypressure_rate} → Overall:{health_rate}"

#(fun-11) hydration level
def hydration_level(weight,water_intake,activity_rate):
    water_recommended= weight*0.033
    if activity_rate=="Moderate":
        water_recommended+= 0.3
    elif activity_rate=="high":
        water_recommended+=0.5
    if water_intake>=water_recommended:
        return "well_hydrated"
    elif water_intake>=(water_recommended*0.8):
        return "slightly hydrated"
    else:
        return "Dehydrated, drink more amounts of water"

#(fun_12) check child growth
def check_child_growth(weight,height,age):
    if age<1:
        ideal_weight= height*0.8
    elif 1<=age<=5:
        ideal_weight=height*0.7
    elif 5<age<=12:
        ideal_weight=height*0.6
    else:
        ideal_weight=height*0.5
    if ideal_weight*0.9<=weight<=ideal_weight*1.1:
        return "Healthy growth"
    elif weight<ideal_weight*0.9:
        return "underweight, you should see a pediatrician"
    else:
        return "overweight, you must see a pediatrician"

#(fun_13) amount of iron required daily
def amount_of_iron_need(age,gender,pregnant=False,breastfeeding=False):
    if age<=1:
        return "you must see a pediatrician "
    elif gender=="male":
        if 2<=age<14:
            return "Recommended iron intake:7 mg/day"
        elif 14<=age<=18:
            return "Recommended iron intake:11 mg/day"
        else:
            return "Recommended iron intake:8 mg/day"
    elif gender=="female":
        if pregnant:
            return "Recommended iron intake during pregnancy:27 mg/day"
        elif breastfeeding:
            return "Recommended iron intake:9 mg/day"
        elif age>=19:
            return "Recommended iron intake:18 mg/day"
        elif 14<=age<=18:
            return "Recommended iron intake:15 mg/day"
        elif age<14:
            return "Recommended iron intake:10 mg/day"

#(fun_14) amount of fiber required daily
def fiber_amount(age,gender,pregnant=False,breastfeeding=False):
    if age<=1:
        return "you must see a pediatrician"
    elif gender=="male":
        if 2<=age<14:
            return "Recommended fiber intake:19 mg/day"
        elif 14<=age<50:
            return "Recommended fiber intake:38 mg/day"
        else:
            return "Recommended fiber intake:30 mg/day"
    elif gender=="female":
        if pregnant:
            return "Recommended fiber intake during pregnancy:28 mg/day"
        elif breastfeeding:
            return "Recommended fiber intake during breastfeeding:29 mg/day"
        elif age<14:
            return "Recommended fiber intake:19 mg/day"
        elif 14<=age<50:
            return "Recommended fiber intake:25 gm/day"
        else:
            return "Recommended fiber intake:21 gm/day"

#(fun_15) calculate and check lean body mass
def check_lean_body_mass(weight,height,gender):
    if gender=="male":
        lbm= (0.407*weight)+(0.267*height)-19.2
    else:
        lbm= (0.252*weight)+(0.473*height)-48.3
    lbm_percentage= (lbm/weight)*100
    if gender=="male":
        if lbm_percentage<60:
            return lbm, "low LBM "
        elif 60<=lbm_percentage<85:
            return lbm, "normal LBM"
        else:
            return lbm, "high LBM"
    else:
        if lbm_percentage<50:
            return lbm, "low LBM"
        elif 50<=lbm_percentage<70:
            return lbm, "normal LBM"
        else:
            return lbm, "high LBM"

#(fun_16) check kidney health
def check_kidney_health(creatinine_level,age,weight,gender):
    if gender=="male":
        gfr= ((140-age)*weight)/(creatinine_level*72)
    else:
        gfr=(((140-age)*weight)/(creatinine_level*72))*0.85
    if gfr>=90:
        return "Normal kidney function"
    elif 60<=gfr<90:
        return "Mild kidney function decline"
    else:
        return "chronic kidney disease, seek medical attention"

#(fun_17) calculate and check BMR
def check_BMR(weight,height,age,gender):
    if gender=="male":
        bmr=88.362+(13.397*weight)+(4.799*height)-(5.677*age)
    elif gender=="female":
        bmr=444.593+(9.247*weight)+(3.098*height)-(4.33*age)
    if bmr<1500:
        bmr_rating= "low BMR"
    elif 1500<=bmr<2000:
        bmr_rating="Average BMR"
    else:
        bmr_rating="high BMR"
    return bmr, bmr_rating

#(fun_18) calculate carbohydrates
def calculate_carbohydrates(bmr,activity_level):
    if activity_level=="inactive":
        TDEE=bmr*1.2
    elif activity_level=="moderate":
        TDEE=bmr*1.55
    elif activity_level=="active":
        TDEE=bmr*1.9
    needed_carbohydrates=(0.5*TDEE)/4
    return needed_carbohydrates

#(fun_19) menstruation_advice
def menstruation_advice(age,period_duration,heavy_bleeding,severe_pain,mode_swings,irregular_periods):
    advice= "Here are some general tips for managing your menstrual cycle"
    if period_duration>7:
        advice+= """your period lasts longer than usual,
          which could indicate a hormonal imbalance and other issues consider seeing a doctor"""
    if heavy_bleeding:
        advice+= """if you are experiencing heavy bleeding,its important to monitor the amount and change your pads frequently 
        if the bleeding excessive(more than 1 pad per hour),consult a doctor"""
    if severe_pain:
        advice+= """it could be a sign of condition like endometriosis or fibroids, consider taking pain
        reivers like ibuprofen, but if the pain is very intense or persistent, see a doctor """
    if mode_swings:
        advice+= """it's common during menstruation due to hormonal changes. 
        engage in relaxing activities and stay hydrated"""
    if irregular_periods:
        advice+= """it could be related to hormonal imbalances or other underlying conditions ,
        its advisable to consult a doctor"""
    if age<18:
        advice += """if you experiencing any usual symptoms,
        such as severe pain or very heavy bleeding its good idea to talk to healthcare professional"""
    if heavy_bleeding and severe_pain:
        advice += " its important to visit a doctor as it could indicate a serious condition"
    return advice

#(fun_20) check muscle strength 
def check_muscle_strength(weight_lifted,repetitions,workout_days):
    strength_score=weight_lifted*repetitions
    if workout_days>=5:
        strength_score*=1.2
    elif workout_days<2:
        strength_score*=0.8
    if strength_score>800:
        return "Excellent muscle strength"
    elif strength_score>400:
        return "Good muscle strength"
    else:
        return "Low ,muscle strength"

