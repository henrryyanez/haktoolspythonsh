Attribute VB_Name = "Módulo1"
Sub EnviarCorreoHTML()
Dim wHoja As Worksheet
Dim Cuerpo As String
Set wHoja = Worksheets("Hoja1")

Dim olApp As Outlook.Application
Set olApp = CreateObject("Outlook.Application")

Dim olMail As Outlook.MailItem
Set olMail = olApp.CreateItem(olMailItem)

Cuerpo = Cuerpo + "<p class=MsoNormal><span style='color:black'>" + "Buen dia Estimado/a" + "&nbsp;" + "<b>" + wHoja.Range("B2").Value + "</b><o:p></o:p></span></p>"
Debug.Print Cuerpo

With olMail
    .To = wHoja.Range("B2").Value
    .Subject = "Correo Prueba Excel"
    .HTMLBody = Cuerpo
    .Send
End With

End Sub
