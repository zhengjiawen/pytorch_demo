# covert text label to xml file
import os
import os.path
import xml.etree.ElementTree as ET

labelDir = 'D:/dataset/icdar2013/Challenge2_Training_Task1_GT/'
debug = False
# icdar2013
def covertToXml(labelPath, resultPath):
    root = ET.Element("tagset")

    dataPosDict, wordRegionNum = convertDataLabel(labelDir, 1)

    for labelKey, labelValue in dataPosDict.items():
        # imageElement = ET.SubElement(root, 'image')
        addImageElement(root, 'imageName', labelValue)


    return root

def addSubElement(root, tag, text):
    element = ET.SubElement(root, tag)
    element.text = text
    element.tail = '\n'

def addRectangleSubElement(root, tag, valueList):
    element = ET.SubElement(root, tag)
    element.set('x', valueList[0])
    element.set('y', valueList[1])
    element.set('width', valueList[2])
    element.set('height', valueList[3])
    element.set('offset', '0')



def addImageElement(root, imgName, valueList):
    imageElement = ET.SubElement(root, 'image')
    addSubElement(imageElement, 'imageName', imgName)
    taggedRectangles = ET.SubElement(imageElement, 'taggedRectangles')
    for value in valueList:
        addRectangleSubElement(taggedRectangles, 'taggedRectangle', value)







def convertDataLabel(path, labelNum=229):
    '''
    covert ICDAR2013 data label, type is text
    :param path: label path
    :param labelNum: data num, the number of icdar 2013 dataset is 229
    :return: dict, key is img name, eg. img name is 100.jpg, the key is 100
    '''
    dataPosDict = {}
    wordRegionNum = 0
    for i in range(labelNum):
        gtPath = path +'gt_'+str(i+100)+'.txt'

        with open(gtPath, 'r') as f:
            posAndValue = []
            for line in f.readlines():

                line = line.strip()
                strs = line.split( )
                posAndValue.append(strs)
                wordRegionNum = wordRegionNum + 1
                # if debug == True:
                #     print(type(strs))
                #     print(strs)
            if debug == True:

                print('posAndValue detail:')
                print('path:'+str(gtPath))
                print('len: '+str(len(posAndValue)))
        dataPosDict[str(i+100)] = posAndValue
    return dataPosDict, wordRegionNum

if __name__ == '__main__':
    root = covertToXml(labelDir, '')
    ET.dump(root)
    # a = 0.9123
    # b = 0.9698
    # c = 2*a*b/(a+b)
    # print(c)