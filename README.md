***ANSYS Scripts Documentation***
--------------

**Overview**
--------------

This repository contains a Python script designed to run after post-processing in ANSYS Mechanical simulations. The script automates the export of images for all Figure objects in the project, with each image named according to the Design Point Number, result name, and analysis name.
Script Details

    Script Name: export.py
    Creation Date: 16-04-24

**Requirements**
--------------

    ANSYS V23+
    Python scripting environment

**Usage**
--------------

   - Ensure that ANSYS Mechanical is installed and the Python scripting environment is set up.
   - Open the ANSYS Mechanical project containing the simulation results you want to export.
   - within the solutions add Python code -> copy & paste
   - set target call back to after solve
   - Ensure that the Design Point of interest is activated.
   - update all design points
   - The script will automatically export images for all Figure objects in the project, saving them in the user_files directory.

**Parameters**
--------------

   - UserFilesDir: The directory where the exported images will be saved. This can be customized as needed.
   - gset: Graphics settings for exporting images, including width, height, and display options.
   - dpn: Design Point Number, used to append to the image name.
   - figures: List of Figure objects in the project.

**Outputs**
--------------

   - Exported images for all Figure objects in the project, saved in the specified directory.
   - Images are named according to the Design Point Number, result name, and analysis name.

**Notes**
--------------

    Ensure that the required Python modules (os, wbjn) are available and properly configured.
    Customize the graphics settings (gset) and file naming conventions (dpn) as needed for your specific requirements.

