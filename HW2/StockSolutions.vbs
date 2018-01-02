Sub Homework()


Dim L As Integer
Dim Sheet As Integer
sheettotal = ThisWorkbook.Worksheets.Count

ActiveWorkbook.Worksheets(1).Activate

For Sheet = 1 To sheettotal


ActiveWorkbook.Worksheets(Sheet).Activate





Dim LastRow As Long
Dim Ticker() As String
Dim Volume() As Long
Dim OpeningValue() As Double
Dim YearlyChange() As Double
Dim PercentageChange() As Double
Dim maxvolume As Long
Dim maxvolumeticker As String
Dim max_percent_increae As Double
Dim maxpercentticker As String
Dim min_percent_increase As Double
Dim minpercentticker As String




Cells(1, 9).Value = "Ticker"
Cells(1, 10).Value = "Yearly Change"
Cells(1, 11).Value = "Percent Change"
Cells(1, 12).Value = "Total Sales Volume"
Cells(1, 16).Value = "Ticker"
Cells(1, 17).Value = "Value"
Cells(2, 15).Value = "Greatest % increase"
Cells(2, 17).NumberFormat = "0.00%"
Cells(3, 15).Value = "Greatest % decrease"
Cells(3, 17).NumberFormat = "0.00%"
Cells(4, 15).Value = "Greatest total volume"



'###################Count the total number of rows with data.######################################
LastRow = Range("A" & Rows.Count).End(xlUp).Row


Count = 0
i = 2



'####################Go through each of the rows (start with row 2) and look for unique ticker symbols##############################
'####################Whenever ticker symbol changes - add one to the ticker total, add the volume; otherwise just add the volume#################

ReDim Preserve OpeningValue(0) As Double
OpeningValue(0) = Cells(2, 3).Value

For i = 2 To LastRow
    If Cells(i + 1, 1).Value <> Cells(i, 1).Value Then
        
        ReDim Preserve Volume(Count)
        ReDim Preserve YearlyChange(Count)
        ReDim Preserve PercentageChange(Count)
        Volume(Count) = Volume(Count) + Cells(i, 7).Value / 100
        YearlyChange(Count) = Cells(i, 6).Value - OpeningValue(Count)
            If OpeningValue(Count) = 0 Then
            PercentageChange(Count) = 0
            Else
            PercentageChange(Count) = Cells(i, 6).Value / OpeningValue(Count) - 1
            End If
        Count = Count + 1
        ReDim Preserve OpeningValue(Count)
        OpeningValue(Count) = Cells(i + 1, 6).Value
        ReDim Preserve Ticker(Count)
        Ticker(Count) = Cells(i, 1).Value
        
        
        

    Else
        ReDim Preserve Volume(Count)
        Count = Count
        Volume(Count) = Volume(Count) + Cells(i, 7).Value / 100
    End If

Next i

'#############Print out the ticker symbols along with their volume################
For j = 0 To Count - 1
Cells(j + 2, 9).Value = Ticker(j + 1)
Cells(j + 2, 12).Value = Volume(j)
Cells(j + 2, 11).Value = PercentageChange(j)
Cells(j + 2, 10).Value = YearlyChange(j)
Next j


'#####################Initialize Values####################
maxvolume = Cells(2, 12).Value
maxvolumeticker = Cells(2, 9).Value
max_percent_increase = Cells(2, 11).Value
maxpercentticker = Cells(2, 9).Value
min_percent_increase = Cells(2, 11).Value
minpercentticker = Cells(2, 9).Value

For k = 1 To Count - 1

If Cells(k + 2, 12).Value > maxvolume Then
maxvolume = Cells(k + 2, 12).Value
maxvolumeticker = Cells(k + 2, 9).Value
Cells(4, 17).Value = maxvolume
Cells(4, 16).Value = maxvolumeticker

Else
Cells(4, 17).Value = maxvolume
Cells(4, 16).Value = maxvolumeticker

End If

If Cells(k + 2, 11).Value > max_percent_increase Then
max_percent_increase = Cells(k + 2, 11).Value
maxpercentticker = Cells(k + 2, 9).Value
Cells(2, 17).Value = max_percent_increase

Else
Cells(2, 17).Value = max_percent_increase
Cells(2, 16).Value = maxpercentticker

End If

If Cells(k + 2, 11).Value < min_percent_increase Then
min_percent_increase = Cells(k + 2, 11).Value
minpercentticker = Cells(k + 2, 9).Value
Cells(3, 17).Value = min_percent_increase

Else
Cells(3, 17).Value = min_percent_increase
Cells(3, 16).Value = minpercentticker

End If

Next k


For L = 1 To Count

plusminus = Cells(L + 1, 11).Value
If plusminus > 0 Then
Cells(L + 1, 11).Interior.ColorIndex = 4
Cells(L + 1, 11).NumberFormat = "0.00%"

Else
Cells(L + 1, 11).Interior.ColorIndex = 3
Cells(L + 1, 11).NumberFormat = "0.00%"

End If

Next L


Next Sheet

End Sub



