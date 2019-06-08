Sub stockdata()

'Variables
Dim rl As Long
Dim openn As Double
Dim closee As Double
Dim max As Double
Dim min As Double

Application.ScreenUpdating = False
ActiveWindow.DisplayGridlines = False

'Contar filas
rl = Cells(Rows.Count, "A").End(xlUp).Row
'encabezados
Cells(1, 9) = "Ticket"
Cells(1, 10) = "Yearly Change"
Cells(1, 11) = "Percent Change"
Cells(1, 12) = "Total Stock Volume"

'contador para valores únicos
s = 2
'valores únicos stocks
For i = 2 To rl
    If Cells(i + 1, 1) <> Cells(i, 1) Then
        Cells(s, 9) = Cells(i, 1)
        s = s + 1
    End If
Next

'Sumar volumen
s = 2
volume = 0
For i = 2 To rl
    If Cells(i + 1, 1) = Cells(i, 1) Then
        volume = volume + Cells(i, 7)
    Else
        volume = volume + Cells(i, 7)
        Cells(s, 12) = volume
        s = s + 1
        volume = 0
    End If
Next

'yearly change n %

openn = Cells(2, 3)

s = 2
'valores cambio yearly
For i = 2 To rl
    If Cells(i + 1, 1) <> Cells(i, 1) Then
        closee = Cells(i, 6)
        Cells(s, 10) = closee - openn
            If (closee - openn) > 0 Then
                Cells(s, 10).Select
                With Selection.Interior
                .Pattern = xlSolid
                .PatternColorIndex = xlAutomatic
                .ThemeColor = xlThemeColorAccent6
                .TintAndShade = 0.599993896298105
                .PatternTintAndShade = 0
                End With
            Else
                Cells(s, 10).Select
                With Selection.Interior
                .Pattern = xlSolid
                .PatternColorIndex = xlAutomatic
                .Color = 8224255
                .TintAndShade = 0
                .PatternTintAndShade = 0
                End With
            End If
        If openn = 0 Then
                Cells(s, 11) = "NA"
        Else
        Cells(s, 11) = (closee - openn) / openn
        End If
        openn = Cells(i + 1, 3)
        s = s + 1
    End If
Next

Columns("J:J").Select
Selection.NumberFormat = "#,##0.0000000000"
Columns("K:K").Select
Selection.NumberFormat = "0.00%"

'encabezados avanzados

    Range("O2").Select
    ActiveCell.FormulaR1C1 = "Greatest % Increase"
    Range("O3").Select
    ActiveCell.FormulaR1C1 = "Greatest % Decrease"
    Range("O4").Select
    ActiveCell.FormulaR1C1 = "Greatest Total Volume"
    Range("P1").Select
    ActiveCell.FormulaR1C1 = "Ticker"
    Range("Q1").Select
    ActiveCell.FormulaR1C1 = "Value"
    
    Columns("O:O").EntireColumn.AutoFit
'nueva última fila

rlm = Cells(Rows.Count, "I").End(xlUp).Row

max = Cells(2, 11)


For i = 3 To rlm
    If Cells(i, 11) = "NA" Then
    ElseIf Cells(i, 11) > max Then
      max = Cells(i, 11)
      Cells(2, 16) = Cells(i, 9)
    End If
Next

min = Cells(2, 11)


For i = 3 To rlm
    If Cells(i, 11) = "NA" Then
    ElseIf Cells(i, 11) < min Then
      min = Cells(i, 11)
      Cells(3, 16) = Cells(i, 9)
    End If
Next

Cells(2, 17) = max
Cells(3, 17) = min

volumem = Cells(2, 12)

For i = 3 To rlm
    If Cells(i, 12) > volumem Then
      volumem = Cells(i, 12)
      Cells(4, 16) = Cells(i, 9)
    End If
Next

Cells(4, 17) = volumem

    Range("Q2:Q3").Select
    Selection.NumberFormat = "0.00%"
    Range("Q4").Select
    Selection.NumberFormat = "General"

End Sub


