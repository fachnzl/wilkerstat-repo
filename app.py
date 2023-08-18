import streamlit as st
import pandas as pd
import requests

st.set_page_config(layout="wide")
with open("css/style.css") as source_des:
    st.markdown(f"<style>{source_des.read()}</style>", unsafe_allow_html=True)


def get_repo_data(idkota):

    cookies = {
        'perf_dv6Tr4n': '1',
        'twk_uuid_624bd5342abe5b455fc4c8f5': '%7B%22uuid%22%3A%221.PUmMTcQdwQkM82WbLdnJHpFJ9zdQTMyMlxTaBaRm8Ffywgsv7wgRLPMtbd50Jlwv1OYv53pnzuAq0MztlA5TH0fO33V0eYWqBAG7IT2mPLDsFYqJn%22%2C%22version%22%3A3%2C%22domain%22%3A%22bps.go.id%22%2C%22ts%22%3A1692175589136%7D',
        'BIGipServerst2023-repo-pro_pool': '2689400842.36895.0000',
        'TS01a10075': '0167a1c861b145afecdc7802c89899977c86791b0df5813ee607bc16825601a66b68b2a43de1779fade059f5e87c213142dd5c43c6',
        'f5_cspm': '1234',
        'XSRF-TOKEN': 'eyJpdiI6IllvalBXdzlaU0dETlRiSFRZcXZsbGc9PSIsInZhbHVlIjoiSnkybmVSV2pKS3JHKzVxY1NpSHA2SFpmcElXcHM5T2d0MGRzVzl5OUNDdDNBb1Yrci9BTDJTUzlWWVJnc2YzTUtJZTRnR010UFZIME55bW8zTE52VzJwbmJmQ2xsK3IzSUovazJQS21tNTBJWGhKZzhDdmdIcW9WZlpNZDNBNVUiLCJtYWMiOiI3ZjNiY2NlZGQ1OTAwNzU3Mzc1YTE1NWMxZmE2ZGI2NGMwM2RiNjA2YWRiZDY2YmJlZDQ0ZmZmYmIzY2I2YjhlIiwidGFnIjoiIn0%3D',
        'st2023_session': 'eyJpdiI6IjFvWHltZDROWDdUUld1WXRPVVA4Z0E9PSIsInZhbHVlIjoiaWFzMGYvY3RkS3pVNGpiaXZ5Z2FVUURZaElSTHZGYldtYkNhVENobWdrV3I0bklOV2N0ZzJIMlpDWC9nQ1BZYXNydWhTRGZOcVd1SmZhVTJWWTNUb3hqc1Y0MHVuSGgvT3M5UCsvUUEwUnNYS3hYTXFlSTE2Zm1kWm53UHJwRHMiLCJtYWMiOiJhYTkyMWU3MzJmYmFjNTYzYTYzZTBkYmNlM2JjZDlkNDBkNTljMjg3N2JjNjZlNTc5MGI0Y2IyNmRmMjMxZDc2IiwidGFnIjoiIn0%3D',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.9',
        'Authorization': 'Bearer 693666|GOxh3tbErNvigW6L8NfQtGLMv3QYYOBmB2Eh5oFc',
        'Connection': 'keep-alive',
        # 'Cookie': 'perf_dv6Tr4n=1; twk_uuid_624bd5342abe5b455fc4c8f5=%7B%22uuid%22%3A%221.PUmMTcQdwQkM82WbLdnJHpFJ9zdQTMyMlxTaBaRm8Ffywgsv7wgRLPMtbd50Jlwv1OYv53pnzuAq0MztlA5TH0fO33V0eYWqBAG7IT2mPLDsFYqJn%22%2C%22version%22%3A3%2C%22domain%22%3A%22bps.go.id%22%2C%22ts%22%3A1692175589136%7D; BIGipServerst2023-repo-pro_pool=2689400842.36895.0000; TS01a10075=0167a1c861b145afecdc7802c89899977c86791b0df5813ee607bc16825601a66b68b2a43de1779fade059f5e87c213142dd5c43c6; f5_cspm=1234; XSRF-TOKEN=eyJpdiI6IllvalBXdzlaU0dETlRiSFRZcXZsbGc9PSIsInZhbHVlIjoiSnkybmVSV2pKS3JHKzVxY1NpSHA2SFpmcElXcHM5T2d0MGRzVzl5OUNDdDNBb1Yrci9BTDJTUzlWWVJnc2YzTUtJZTRnR010UFZIME55bW8zTE52VzJwbmJmQ2xsK3IzSUovazJQS21tNTBJWGhKZzhDdmdIcW9WZlpNZDNBNVUiLCJtYWMiOiI3ZjNiY2NlZGQ1OTAwNzU3Mzc1YTE1NWMxZmE2ZGI2NGMwM2RiNjA2YWRiZDY2YmJlZDQ0ZmZmYmIzY2I2YjhlIiwidGFnIjoiIn0%3D; st2023_session=eyJpdiI6IjFvWHltZDROWDdUUld1WXRPVVA4Z0E9PSIsInZhbHVlIjoiaWFzMGYvY3RkS3pVNGpiaXZ5Z2FVUURZaElSTHZGYldtYkNhVENobWdrV3I0bklOV2N0ZzJIMlpDWC9nQ1BZYXNydWhTRGZOcVd1SmZhVTJWWTNUb3hqc1Y0MHVuSGgvT3M5UCsvUUEwUnNYS3hYTXFlSTE2Zm1kWm53UHJwRHMiLCJtYWMiOiJhYTkyMWU3MzJmYmFjNTYzYTYzZTBkYmNlM2JjZDlkNDBkNTljMjg3N2JjNjZlNTc5MGI0Y2IyNmRmMjMxZDc2IiwidGFnIjoiIn0%3D',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
        'X-XSRF-TOKEN': 'eyJpdiI6IllvalBXdzlaU0dETlRiSFRZcXZsbGc9PSIsInZhbHVlIjoiSnkybmVSV2pKS3JHKzVxY1NpSHA2SFpmcElXcHM5T2d0MGRzVzl5OUNDdDNBb1Yrci9BTDJTUzlWWVJnc2YzTUtJZTRnR010UFZIME55bW8zTE52VzJwbmJmQ2xsK3IzSUovazJQS21tNTBJWGhKZzhDdmdIcW9WZlpNZDNBNVUiLCJtYWMiOiI3ZjNiY2NlZGQ1OTAwNzU3Mzc1YTE1NWMxZmE2ZGI2NGMwM2RiNjA2YWRiZDY2YmJlZDQ0ZmZmYmIzY2I2YjhlIiwidGFnIjoiIn0=',
        'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    response = requests.get(
        f'https://st2023-repo.bps.go.id/api/monitoring-master/{idkota}', cookies=cookies, headers=headers)

    return(response.json())


try:
    last_update = pd.read_csv("data/last_update.csv")
    st.markdown("Terakhir Update " + last_update["0"][0])
    try:
        repo_json = get_repo_data('1174')['data']
        repo = pd.DataFrame.from_dict(repo_json)
        # st.table(repo.head())
    except:
        repo = pd.read_csv("data/repo.csv")

    wilkerstat = pd.read_csv("data/wilkerstat.csv")

    if wilkerstat["nm_project"][0].astype(str).startswith("000"):
        wilkerstat['idsubsls'] = wilkerstat['iddesa'].astype(
            str)+wilkerstat['nm_project'].astype(str)
    else:
        wilkerstat['idsubsls'] = wilkerstat['iddesa'].astype(
            str)+"000"+wilkerstat['nm_project'].astype(str)
    col1, col2, col3, col4 = st.columns(4)
    col1.markdown("Jumlah SLS/Non SLS Repo")
    col1.markdown(len(repo))
    col2.markdown("Jumlah UTP (R305) Repo")
    col2.markdown(sum(repo['b305']))
    col3.markdown("Jumlah Project Wilkerstat")
    col3.markdown(len(wilkerstat.groupby('idsubsls').count()))
    col4.markdown("Jumlah ART Pertanian")
    col4.markdown(sum(wilkerstat['jumlah_art_tani']))

    wilkerstat_sum = wilkerstat.groupby(['idsubsls'])['jumlah_art_tani'].sum()
    wilkerstat_count = wilkerstat.groupby(
        ['idsubsls'])['jumlah_art_tani'].count()
    wilkerstat_subsls = pd.DataFrame(
        {'jumlah_tagging': wilkerstat_count, 'jumlah_art_tani': wilkerstat_sum})
    wilkerstat_subsls.index.name = 'idsubsls'
    wilkerstat_subsls.reset_index(inplace=True)
    repo_subsls = pd.DataFrame(
        repo.loc[:, ['idsubsls', 'nmsls', 'b305', 'nama_petugas']])
    repo_subsls['idsubsls'] = repo_subsls['idsubsls'].astype(str)
    wilkerstat_subsls['idsubsls'] = wilkerstat_subsls['idsubsls'].astype(str)
    new_pml = pd.read_excel("data/daftar pml.xlsx").iloc[:, [1, 2]]
    new_pml['idsubsls'] = new_pml['idsubsls'].astype(str)
    # st.table(new_pml)
    # wilkerstat_subsls['jumlah_tagging'] = wilkerstat_subsls['jumlah_tagging'].astype(int)
    # wilkerstat_subsls['jumlah_art_tani'] = wilkerstat_subsls['jumlah_art_tani'].astype(int)
    col1 = st.container()
    pmls = col1.multiselect('Filter by PML', ['Muhammad Bohari Rahman S.Stat.', 'Nadya Husna S.Tr.Stat.', 'Muhammad Ikhwani', 'Muhammad Fachry Nazuli S.Tr.Stat.', 'Ema Juniati SST', 'Hera Lestari S.Si', 'Iryani', 'Chalida Rahmi SE, M.M.', 'Yusra S.E', 'Salviyana Nurdin A.Md', 'Suci Maulida SST'], [
                            'Muhammad Bohari Rahman S.Stat.', 'Nadya Husna S.Tr.Stat.', 'Muhammad Ikhwani', 'Muhammad Fachry Nazuli S.Tr.Stat.', 'Ema Juniati SST', 'Hera Lestari S.Si', 'Iryani', 'Chalida Rahmi SE, M.M.', 'Yusra S.E', 'Salviyana Nurdin A.Md', 'Suci Maulida SST'])
    try:
        filterpml = ''
        for pml in pmls:
            filterpml = filterpml + "'" + pml+"', "
        filterpml = filterpml[:-2]
    except:
        st.markdown("PML Belum dipilih")
    data_merge = repo_subsls.merge(
        wilkerstat_subsls, how="left", on='idsubsls')
    data_merge['jumlah_tagging'] = data_merge['jumlah_tagging'].fillna(
        0).astype(int)
    data_merge['jumlah_art_tani'] = data_merge['jumlah_art_tani'].fillna(
        0).astype(int)
    data_merge = data_merge.merge(new_pml, how="left", on='idsubsls')
    # st.table(data_merge)

    data_merge = data_merge.query("nama_pml_new in ("+filterpml+")")
    # st.container().table(data_merge)

    display_table = """
                <table>
                    <thead>
                        <tr>
                            <th>No</th>
                            <th>ID SubSLS</th>
                            <th>Nama SLS</th>
                            <th>UTP Repo (R305)</th>
                            <th>Jumlah Tagging</th>
                            <th>Jumlah ART Tani Wilkerstat</th>
                            <th>Nama PML</th>
                            <th>Status</th>
                        </tr>
                    </thead>
                    <tbody>
                    """

    table_row = ""
    i = 0
    for idx in data_merge.index:
        i = i+1
        if data_merge['b305'][idx] == data_merge['jumlah_art_tani'][idx]:
            status = "Repo sama dengan Wilkerstat"
            color_status = "green"
        else:
            status = "Repo berbeda dengan Wilkerstat"
            color_status = "red"
        table_row = table_row + \
            f"<tr><td>{i}</td><td>{data_merge['idsubsls'][idx]}</td><td>{data_merge['nmsls'][idx]}</td><td>{data_merge['b305'][idx]}</td><td>{data_merge['jumlah_tagging'][idx]}</td><td>{data_merge['jumlah_art_tani'][idx]}</td><td>{data_merge['nama_pml_new'][idx]}</td><td><span style='color:{color_status};'>{status}</span></td></tr>"
    # st.markdown(table_row)
    display_tables = f"{display_table}{table_row}</tbody></table>"
    st.markdown(display_tables, unsafe_allow_html=True)
except:
    st.markdown("Data Belum di update")
