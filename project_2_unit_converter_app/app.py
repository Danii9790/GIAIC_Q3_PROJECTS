import streamlit as st
# Unit converter app:

def covert_unit(value:float,unit_form:str,unit_to:str):
    # print("Value>> ",value)
    # print("unit_form>> ",unit_form)
    # print("unit_to>> ",unit_to)

    if unit_form == "kilometers" and unit_to == "meters":
        return value * 1000
    elif unit_form == "meters" and unit_to =="kilometers":
        return value * 0.001
    elif unit_form == "kilograms" and unit_to == "grams":
        return value * 1000
    elif unit_form == "grams" and unit_to == "kilograms":
        return value * 0.001
    else:
        return "conversion is not supported"
    
# Hard Coded Method: 
# result1=covert_unit(2.5,"kilometers","meters")
# print("Result Value is : ",result1)
# result2=covert_unit(4000,"grams","kilograms")
# print("Result Value is : ",result2)

# Input Function or console base application:
def main():
    st.set_page_config(page_title="Unit_Conveter_App😉")
    st.title("Welcome to Unit Converter App😎")
    st.write("You can convert your values easily by using this App")
    value=st.number_input("Enter your Number you want to Convert : ",min_value=0    )
    unit_form=st.text_input("Enter a value to want to convert from (e.g: meters,kilometers,grams,kilograms)")
    unit_to=st.text_input("Enter a value to want to convert to (e.g: meters,kilometers,grams,kilograms)")

    if st.button("Convert"):
        result =covert_unit(value,unit_form,unit_to)
        st.write("Converted Value is :",result)
# Without using Streamlit libary or console base Applilcation method:
    # print("Welcome To Unit Conveter App")
    # value=float(input("Enter a value you want to convert : "))
    # unit_from=input("Enter a value to want to convert from (e.g: meters,kilometers,grams,kilograms)")
    # unit_to=input("Enter a value to want to convert to (e.g: meters,kilometers,grams,kilograms)")

    # print("Value : ",value)
    # print("Unit_From : ",unit_from)
    # print("Unit_To : ",unit_to)
    # result=covert_unit(value,unit_from,unit_to)
    # print(result)

main()