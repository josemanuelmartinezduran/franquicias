import uploader, format
format_list = []
u = uploader.uploader()
u.upload("product.template", format_list, 2, 10000, "product.csv")