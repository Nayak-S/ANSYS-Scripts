def after_post(this, solution):# Do not edit this line
    #import modules
    import os
    import wbjn

    #Get Design Point Number as Text (to append it to the image name)
    dpn=wbjn.ExecuteCommand(ExtAPI,"returnValue(a+Parameters.GetActiveDesignPoint().Name)",a="DP")

    #Get the User Files Directory of the Project to save images. Ofcourse you can use any path you like.
    UserFilesDir = wbjn.ExecuteCommand(ExtAPI,"returnValue(GetUserFilesDirectory())")

    #Some Graphics Settings
    gset = Ansys.Mechanical.Graphics.GraphicsImageExportSettings()
    gset.CurrentGraphicsDisplay = False
    gset.Width = 1920
    gset.Height = 1080

    for analysis in ExtAPI.DataModel.AnalysisList:
        #Get All Equivalent Stress Objects in all the Analyses in the Tree
        #EqvStressResults = [child for child in analysis.Solution.Children if child.DataModelObjectCategory == DataModelObjectCategory.EquivalentStress]

        #Get All Total Deformation Objects in all the Analyses in the Tree
        #TotalDeformationResults = [child for child in analysis.Solution.Children if child.DataModelObjectCategory == DataModelObjectCategory.TotalDeformation]
        
        #figures=ExtAPI.DataModel.GetObjectsByType(DataModelObjectCategory.Figure)
        figures=ExtAPI.DataModel.GetObjectsByType(DataModelObjectCategory.Figure)

        AllResults = figures # [ add if TotalDeformationResults & EqvStressResults are requried]

        for result in AllResults:
            result.Activate()
            fName=dpn+"_"+result.Name+"_" + analysis.Name+".png"
            fPath = os.path.join(UserFilesDir, fName)
            if os.path.exists(fPath):
                os.remove(fPath)
            Graphics.ExportImage(fPath, GraphicsImageExportFormat.PNG, gset)