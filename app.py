import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
with open("css/style.css") as source_des:
    st.markdown(f"<style>{source_des.read()}</style>", unsafe_allow_html=True)

# try:
    last_update = pd.read_csv("data/last_update.csv")
    st.markdown("Terakhir Update " + last_update["0"][0])
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
    repo_subsls = pd.DataFrame(repo.iloc[:, [0, 7, 22, 25]])
    repo_subsls['idsubsls'] = repo_subsls['idsubsls'].astype(str)
    wilkerstat_subsls['idsubsls'] = wilkerstat_subsls['idsubsls'].astype(str)
    # new_pml = pd.read_excel(repo_upload)
    # wilkerstat_subsls['jumlah_tagging'] = wilkerstat_subsls['jumlah_tagging'].astype(int)
    # wilkerstat_subsls['jumlah_art_tani'] = wilkerstat_subsls['jumlah_art_tani'].astype(int)
    col1 = st.container()
    pmls = col1.multiselect('Filter by PML', ['Muhammad Bohari Rahman S.Stat.', 'Nadya Husna S.Tr.Stat.','Muhammad Ikhwani' ,'Muhammad Fachry Nazuli S.Tr.Stat.', 'Ema Juniati SST','Hera Lestari S.Si','Iryani','Chalida Rahmi SE, M.M.','Yusra S.E','Salviyana Nurdin A.Md','Suci Maulida SST'],['Muhammad Bohari Rahman S.Stat.', 'Nadya Husna S.Tr.Stat.','Muhammad Ikhwani' ,'Muhammad Fachry Nazuli S.Tr.Stat.', 'Ema Juniati SST','Hera Lestari S.Si','Iryani','Chalida Rahmi SE, M.M.','Yusra S.E','Salviyana Nurdin A.Md','Suci Maulida SST'])
    try:
        filterpml = ''
        for pml in pmls:
            filterpml = filterpml +"'"+ pml+"', "
        filterpml = filterpml[:-2]   
    except: 
        st.markdown("PML Belum dipilih")
    data_merge = repo_subsls.merge(wilkerstat_subsls, how="left", on='idsubsls')
    data_merge['jumlah_tagging'] = data_merge['jumlah_tagging'].fillna(0).astype(int)
    data_merge['jumlah_art_tani'] = data_merge['jumlah_art_tani'].fillna(0).astype(int)
    data_merge = data_merge.query("nama_pml in ("+filterpml+")")
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
        table_row = table_row + f"<tr><td>{i}</td><td>{data_merge['idsubsls'][idx]}</td><td>{data_merge['nmsls'][idx]}</td><td>{data_merge['b305'][idx]}</td><td>{data_merge['jumlah_tagging'][idx]}</td><td>{data_merge['jumlah_art_tani'][idx]}</td><td>{data_merge['nama_pml'][idx]}</td><td><span style='color:{color_status};'>{status}</span></td></tr>"
    # st.markdown(table_row)    
    display_tables = f"{display_table}{table_row}</tbody></table>"
    st.markdown(display_tables, unsafe_allow_html=True)
# except:
#     st.markdown("Data Belum di update")
