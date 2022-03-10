Steps：
1. install python package firstly:
pip install html-testRunner
pip install requests
pip install json

2. Get my projects: git clone https://github.com/AmyZhang0703/PycharmProjects.git

3. Run my scipts: 
\PycharmProjects\APIUnitTest\UnitTest.py
TestResults: PycharmProjects\TestResults\TestResults___main__.UnitTests_2022-03-10_17-03-17.html

4. trouble shooting you may meet:
TestResults: PycharmProjects\TestResults\TestResults___main__.UnitTests_2022-03-10_17-03-17.html "View" button can't be opened.
It is because "jQuery" can't be load.

soluation:
Go to python lib: example:
C:\Python39\Lib\site-packages\HtmlTestRunner\template\report_template.html

Edit the files in line 142:

 old: <!--script src="https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js"></script-->
new : <script src="https://lib.sinaapp.com/js/jquery/2.0.2/jquery-2.0.2.min.js"></script>

5. Others:
The projects can be improved: we can use python "ddt" to do data manament. I didn't do it as time limitted.

Any suggestions is welcomed!
Thanks!
