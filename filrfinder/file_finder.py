import os
import xlrd3 as xl
import xlwt

dirpath2 = 'D:/途/OpenCv/项目材料/snapshot_total' #存放图片的文件夹
dirpath1 = 'D:/途/OpenCv/项目材料/交付汇总-5901/游戏-568' #存放图片的文件夹
datapath = 'D:/途/OpenCv/项目材料/对应关系表.xlsx' #excel表路径

def readExcel(filname,sheetname):
    xls_file = xl.open_workbook(filname)  # 打开文件
    xls_sheet = xls_file.sheet_by_name("Sheet1")  # 通过工作簿名称获
    cv0 = xls_sheet.col_values(0)  # 第一行所有的值
    cv1 = xls_sheet.col_values(1)  # 第二列所有的值
    cv2 = xls_sheet.col_values(2)  # 第三列所有的值

def renameImg1(srcImgDir):
    xls_file = xl.open_workbook(datapath)  # 打开文件
    xls_sheet = xls_file.sheet_by_name("Sheet1")  # 通过工作簿名称获
    cv0 = xls_sheet.col_values(0)  # 第一行所有的值
    cv1 = xls_sheet.col_values(1)  # 第二列所有的值
    cv2 = xls_sheet.col_values(2)  # 第三列所有的值

    filelist=os.listdir(dirpath1)

    for spices in range(len(cv0)):
        if cv0[spices]=="游戏-568":
           #for index in range(len(cv1)):
              for file in filelist:
                  Olddir = os.path.join(dirpath1, file)
                  filename = os.path.splitext(file)[0]
                  filetype = os.path.splitext(file)[1]
                  if filename+filetype==cv1[spices]:
                      #print("match"+filename+cv1[spices])
                      newF = os.path.join(dirpath1, str(cv0[spices]) + "_" + "original" + "+" + filename + filetype)
                      os.rename(Olddir,newF)
                      print("successfully in 1")
                  else:
                      continue
        else:
            continue

def renameImg2(srcImgDir):
    xls_file = xl.open_workbook(datapath)  # 打开文件
    xls_sheet = xls_file.sheet_by_name("Sheet1")  # 通过工作簿名称获
    cv0 = xls_sheet.col_values(0)  # 第一行所有的值
    cv1 = xls_sheet.col_values(1)  # 第二列所有的值
    cv2 = xls_sheet.col_values(2)  # 第三列所有的值

    filelist=os.listdir(dirpath2)

    for index in range(len(cv2)):
        for file in filelist:
            Olddir = os.path.join(dirpath2, file)
            filename = os.path.splitext(file)[0]
            filetype = os.path.splitext(file)[1]
            if cv2[index]==filename:
               #print("match"+cv2[index]+"__"+filename)
               #print(cv0[index])
               #print(cv2[index])
               newF = os.path.join(dirpath2, str(cv0[index]) + "_" + "Photo" + "+" + cv1[index])
               os.rename(Olddir,newF)
               print("successfully in 2")
            else:
                continue


if __name__ == '__main__':
    readExcel(datapath,"Sheet1")
    #renameImg1(dirpath1)
    #renameImg2(dirpath2)
