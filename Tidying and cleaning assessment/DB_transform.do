
// Jorge De León - jdeleonxz@gmail.com 

// we set our working directory where we downloaded the files and where we will upload the new file 


cd "C:\Users\Jorge De León\Desktop\Master\Metodos computacionales para politicas publicas\MCPP\Tidying and cleaning assessment"

// The command is to import the database in csv format. 

import delimited "mother_survey.csv"

// We want to create a new table where every observation is a child 

egen int new_obs = total(n_children)

// we see we have 312 children so we want to create a new table where every observations is a children


// using reshape sex in_school yob grade


egen id = seq(), from(1)

reshape long age_ sex_ in_school_ yob_ grade_, i(id) j(n) string 

save "new_mother_surveys.dta", replace

// we have reshaped the data into long format but we have a many missing values. As we saw before we only have a total of 312 children and the reshape function took as if we have 6 children for every mother, but we only have data for the children every mother has, the rest are missing values that we can eliminate from the database 

clear 

use "new_mother_surveys.dta"

tabulate age_

drop if age_ == "NA"

// Now we check the values of each column 

tabulate sex_

foreach i in sex_ {
	replace sex_ = "Male" if `i' == "male"
	replace sex_ = "Male" if `i' == "M"
	replace sex_ = "Female" if `i' == "female"
	replace sex_ = "Female" if `i' == "F"
}

tabulate sex_

// Now sex only has two categories 

tabulate in_school_

tabulate yob_

// we have a 9999 value that is an error. We can manage this value with a simple operation. 2022 - age. 

destring age_, replace
destring yob_, replace

foreach i in yob_ {
	replace yob_ = 2022- age_ if `i' == 9999
}

tabulate yob_

tabulate grade_
tabulate in_school_

// first we have one value in grade_ with -99 for a child who is not at school. that should be a missing value. 

// Lets see is there is any relation between age and grade to manage the other -99 values. 

tabulate age_ grade_ 

// age 0 is the missing in grade_ that has -99 value.
// child between 3 and 6 years old are most likely to be in first grade. We can this to every age and have the following relationship:


foreach i in grade_ {
	replace grade_ = "NA" if age_ == 0 & `i' == "-99"
	replace grade_ = "1" if age_ == 3 & `i' == "-99"
	replace grade_ = "1" if age_ == 4 & `i' == "-99"
	replace grade_ = "1" if age_ == 5 & `i' == "-99"
	replace grade_ = "1" if age_ == 6 & `i' == "-99"
	replace grade_ = "2" if age_ == 7 & `i' == "-99"
	replace grade_ = "3" if age_ == 8 & `i' == "-99"
	replace grade_ = "4" if age_ == 9 & `i' == "-99"
	replace grade_ = "5" if age_ == 10 & `i' == "-99"
	replace grade_ = "6" if age_ == 11 & `i' == "-99"
	
}

tabulate grade_

// Now we have cleared and transform the database into a form easy to work with. 

// we save the .dta archive

drop n n_children new_obs

// We do not eliminate the id variable because that corresponds to a children or a group of children from the same mother_ID AND village_ID.

rename age mother_age
rename yob mother_yob
rename educ mother_educ

// Every obervation contains the information of one child. the information of his mother including id and village id, and his information. 

save "new_mother_surveys.dta", replace
