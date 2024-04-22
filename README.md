# Golab_Remitly
This is a repository for a Remitly Internship 2024 task created by Witold Gołąb (tolek.golab@gmail.com):</br>
https://docs.google.com/forms/d/e/1FAIpQLSdKmVI3bmsu6ylz345V5mj--cSQ9TaPhA0ILk9S-_QJCFHihA/viewform
</br></br>
Steps to open the solution:</br>
1. Download this repository.</br>
2. Open https://www.online-python.com/ in an Internet browser.</br>
3. On the website from (2.) open all files from the repository one by one using Open file From Disk option (button with directory).</br>
   ![image](https://github.com/Thejter/Golab_Remitly/assets/20191225/df855f27-c0ff-45e9-af15-11ed01b94465)
4. Open main_GolabWitold.py file.</br>
5. Click green Run button (located underneath main_GolabWitold.py file) to run test.</br>
  ![image](https://github.com/Thejter/Remitly_Golab/assets/20191225/00b811af-8e8a-4f6a-966e-228f4c7fa82c)
6. Tests results:</br>
![image](https://github.com/Thejter/Remitly_Golab/assets/20191225/a252e320-4d72-465e-bae1-bc69be091427)
    Tests fail if:</br>
    - Resource field contains anything else or is empty</br>
    - Could not open file</br>
    - JSON file is not compatible with AWS::IAM::Role Policy</br>

Tests pass if could open file and JSON file is compatible with AWS::IAM::Role Policy and Resource field is equal to "*".
