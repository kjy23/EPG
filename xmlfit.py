import requests
import xml.etree.ElementTree as ET

# EPG 文件的 URL 列表
epg_urls = [
    "https://raw.githubusercontent.com/kjy23/EPG/refs/heads/master/epgs/daddylive-channels-epg.xml",
    "https://epg.iill.top/epg",
    "https://tvpass.org/epg.xml",
    "https://assets.livednow.com/epg.xml",
    "https://xutv.486253.xyz/xumo/epg.xml",
    "https://raw.githubusercontent.com/azimabid00/epg/main/astro_epg.xml",
    "https://github.com/dtankdempse/daddylive-m3u/raw/refs/heads/main/epg.xml",
    "https://dis.486253.xyz/distrotv/epg.xml",
    "https://epgshare01.online/epgshare01/epg_ripper_JP1.xml.gz",
    "https://epgshare01.online/epgshare01/epg_ripper_JP2.xml.gz",
    "https://epg.djtmewibu.com/jcom.xml",
    "https://i.mjh.nz/PBS/all.xml.gz",
    "https://github.com/matthuisman/i.mjh.nz/raw/master/Plex/all.xml.gz",
    "https://github.com/matthuisman/i.mjh.nz/raw/master/PlutoTV/all.xml.gz",
    "https://github.com/matthuisman/i.mjh.nz/raw/master/Roku/all.xml.gz",
    "https://github.com/matthuisman/i.mjh.nz/raw/master/SamsungTVPlus/all.xml.gz",
    "https://i.mjh.nz/Stirr/all.xml.gz",
    "https://github.com/dtankdempse/tubi-m3u/raw/refs/heads/main/tubi_epg_us.xml"
]

# 合并后的 EPG 文件输出路径
output_file = "merged_epg.xml"

# 用于存储所有节目条目的列表
all_programs = []

# 解析 XML 数据
def parse_epg_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        xml_data = response.text
        
        # 解析 XML 内容
        root = ET.fromstring(xml_data)
        
        # 假设节目条目位于 "programme" 标签中
        for programme in root.findall("programme"):
            all_programs.append(programme)
        
    except Exception as e:
        print(f"Error fetching or parsing {url}: {e}")

# 合并所有 EPG 文件
for url in epg_urls:
    parse_epg_url(url)

# 创建合并后的 XML 文件
root = ET.Element("tv")  # 新的 XML 根节点

# 将所有节目条目添加到根节点中
for program in all_programs:
    root.append(program)

# 创建新的 XML 树并写入文件
tree = ET.ElementTree(root)
tree.write(output_file)

print(f"EPG files have been merged into {output_file}")
