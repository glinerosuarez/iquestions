"""
The following dataset http://url4828.interviewqs.com/ls/click?upn=qwT-2Bl0U064-2B7oRNpPgUya51JFUDgj241ZqJOHGqS8eD4tjNEUUiE84jSUq3UK-2FXXCI-2FS0fZ3xFQdjhUDh8xz-2BuhsFB1mH1862nQ-2FY4ZybvMF-2F2cs0iOwKCE8rVHQUKQUuB4A_Rnksh8mmH7vi3d5oyhplLP4H0bOosjDG5cWn-2BNVdc5OsSAq1-2F8Xb8hE6ay4samejco0sA0AHGEKJIJon3pKPuqaTXwrirFQyhq0D-2F0BGFmZU4yCFR9PoCghvqDdNtrXBj-2F5MlgQS-2FZdU8EdpcB4kFn3zNDDfUQMzXBUTNBKk-2B4imRaeb-2BKoPLopQ4SmiD-2FWy0Asv5YYoiPELvGriPtY979ivgsUMegn7ZgF-2FspD19nAOuo3M6yoF-2BCpzYRxBiW-2Fi5S7D3BBBNz6R81Yqmc5RXgzEDWSWCdRzavnka4pWQA1VjoOICq19JV6ka7Ch3uZUHg6Hwc7a-2BoEVQw0HDVNjDh7ngnnICSwvTJUkP0bLpZf48-2FNc5PRwCGc9t5jJValR
contains the following fields that describe employee attrition for a company:

satisfaction_level: value between 0 - 1 that describes how satisfied the employee was at their current role
last_evaluation: value between 0 - 1 that describes how well the employee performed
number_project: number of projects the employee was on
average_montly_hours: average number of hours worked monthly time_spend_company: number of years at the company
work_accident: boolean for if the employee has been in an accident at work
left: boolean that describes if the employee has left the company
role: employee's role
salary: low, medium, high --> indicates how high employee salary was
Can you describe which factors are the strongest indicator if an employee is going to attrit?
Hint: If you're having trouble finding a starting point, you can reference this method and this wikipedia page.
http://url4828.interviewqs.com/ls/click?upn=qwT-2Bl0U064-2B7oRNpPgUya5QQs9B7-2B1rj96Ze-2FjztJuc-2FrL4f9w3VpVhBp0MoA05isugHEk-2FQlJ-2BIqoe7T4Pvhp9K8H8tkr7V2hA4LgFuR-2BpWY-2FGU0WIV5RGcxhF99wTSOsYv_Rnksh8mmH7vi3d5oyhplLP4H0bOosjDG5cWn-2BNVdc5OsSAq1-2F8Xb8hE6ay4samejco0sA0AHGEKJIJon3pKPuqaTXwrirFQyhq0D-2F0BGFmZU4yCFR9PoCghvqDdNtrXBj-2F5MlgQS-2FZdU8EdpcB4kFn3zNDDfUQMzXBUTNBKk-2B4imRaeb-2BKoPLopQ4SmiD-2FWy0Asv5YYoiPELvGriPtY979ivgsUMegn7ZgF-2FspD19nDX6hTmIV1sn7rFXsmp0-2BzShWP7f01DfrL-2Fgh0aKXNMyIs-2BBztvWTSkAZ-2BtO6HlzfB90ZfT216s-2BClGcnb-2BemCrUROMWe-2BuIU2YnTduDwNCrTRBZv-2BlO94PhSLiIvKZw3x7vR6eWvZj0aA8l-2FAOVn5k
http://url4828.interviewqs.com/ls/click?upn=qwT-2Bl0U064-2B7oRNpPgUya2MDSsqRZgJKYpdTORZxvd78R0SouieZzBStI9aFFVLAp75Q3SMLkPTHSEviuDW5zMnbpmJXn-2FRovX2gQSdtrBA-3DkWs3_Rnksh8mmH7vi3d5oyhplLP4H0bOosjDG5cWn-2BNVdc5OsSAq1-2F8Xb8hE6ay4samejco0sA0AHGEKJIJon3pKPuqaTXwrirFQyhq0D-2F0BGFmZU4yCFR9PoCghvqDdNtrXBj-2F5MlgQS-2FZdU8EdpcB4kFn3zNDDfUQMzXBUTNBKk-2B4imRaeb-2BKoPLopQ4SmiD-2FWy0Asv5YYoiPELvGriPtY979ivgsUMegn7ZgF-2FspD19nCgUQoup2xjO9yUplDA1uEEGl3-2FdmZqXYzazaRKDdWkJ2iWLHxznuiq8Xr-2BGolgshAuemgF9QT5A71Vr7PZujJo1ri3bjYAfxH3xGDg2ZoX0UDPqWX5aabRTt3DtmrdEwLULUz3wiA-2F9Pp-2BVRr5tWx1
"""