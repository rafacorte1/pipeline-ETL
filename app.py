import requests

def fetch_page():
    url = "https://www.amazon.com.br/Headphone-Ouvido-HV-H2002d-Microfone-Falante/dp/B07Y2G7VX5/?_encoding=UTF8&pd_rd_w=wQL3o&content-id=amzn1.sym.8fbb3d34-c3f1-46af-9d99-fd6986f6ec8f&pf_rd_p=8fbb3d34-c3f1-46af-9d99-fd6986f6ec8f&pf_rd_r=40YN1HNRH98MAJYD5EM5&pd_rd_wg=YjRag&pd_rd_r=49c427ad-ba07-4315-904b-8347eb8f5aac&ref_=pd_hp_d_btf_crs_zg_bs_7791985011"
    response = requests.get(url)
    return response.text

if __name__ == "__main__":
    page_content = fetch_page()
    print(page_content)