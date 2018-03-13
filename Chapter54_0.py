import urllib.request
import easygui as g


def input_wid_hei():
    fieldnames = ["宽:", "高:"]
    field_values = g.multenterbox("请填写喵的尺寸", "下载一只喵", fieldnames)
    return field_values


def save_image(content):
    file_path = g.diropenbox("请选择存放喵的文件夹:")
    with open(file_path + '//' + 'cat.jpg', 'wb') as f:
        f.write(content)


def get_url():
    list_cord = input_wid_hei()
    response = urllib.request.urlopen("http://placekitten.com/g/" + list_cord[0] + "//" + list_cord[1])
    cat_img = response.read()
    return cat_img


def main():
    cat = get_url()
    save_image(cat)


if __name__ == '__main__':
    main()
