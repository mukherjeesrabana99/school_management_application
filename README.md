# school_management_application
This school app allows only the school administrator to manage every system, for the time being. More functionalities will be added later.
# Folder Structure 
0.academics/accounts/address/administration/events/faculty/notice/online_tests/results/sports/students/timetable --each of these apps are created using python manage.py 
startapp command.
1.Each of these apps contains built in views.py and models files for writing logics to connect the frontend and the models in the models.py file and for 
creating models respectively.
2.Two more files urls.py and forms.py are added to each of these apps to define the urlpatterns and to make forms using django forms respectively.
3.The folder 'school_software'and the file manage.py  are autogenerated after a django project called 'school_software' is initialized.
This folder contains a urls.py built in within itself to define url patterns and include urls of other apps as well.Views.py is created in a view to rendering home page.
4.Lastly the 'templates' and 'static' folders are created, and kept maintaing the same directory level with those app folders.
a>template folder further contains all the folders that are created corresponding to each of the above mentioned apps, to render their respective html pages.
i>'base.html' contains code that renders the components which are common for each of the html templates like navbar, dashboard, footer, header etc.
ii>'home.html' contains code for rendering home page
b>static folder contains all css javascript files, images, which are used in the html pages to render images and styling.

# Admin-Dashboard
0. Admin can view the currently running sessio and 
the school name appearing in the navbar 
1. Admin can view the number of classes, sections, shifts, subjects and registered classes
2. Admin can view the number of students
3. admin can view the number of teachers
4. Admin can view the number of events
5. Admin can view the number of onging/scheduled/completed exams
# Admin-Academics Management
 Admin can add/edit/delete /view classes sections, sessions, shifts, subjects and registered classes


Also Admin can add/edit/delete/view addresses , which the admin,  a student or a teacher can take referrence from, while filling the address field in the respective registration
forms.



# Admin-Student Management
0.  Admin can add/view/edit/delete students
1.  Admin can accept/reject/view a student waiting to get admitted to the school
# Admin-Teacher Management
 Admin can add/view/edit/delete teachers
# Admin-Event Management
Admin can add/edit/view/delete events, event categories, event agenda and event member
# Admin-Exam Management. 
Admin can add/edit/delete/view results for each student but one subject at a time
# Admin-Notice Management
Admin can add/edit/delete/view notice
# Admin-Fees Management
Admin can add/edit/delete/view fees structure for each class, view payment status of each student class-wise
# Admin-Timetable management
Admin can add/edit/delete/view timetables for each registered class

# Drawbacks
0. While creating the timetable model the subjects are required  to be 
be hardcoded,which needs to be fixed
1.While creating result, multiple subjects can't be chosen
at a time, which too needs to be fixed.



