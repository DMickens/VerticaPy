"""
(c)  Copyright  [2018-2023]  OpenText  or one of its
affiliates.  Licensed  under  the   Apache  License,
Version 2.0 (the  "License"); You  may  not use this
file except in compliance with the License.

You may obtain a copy of the License at:
http://www.apache.org/licenses/LICENSE-2.0

Unless  required  by applicable  law or  agreed to in
writing, software  distributed  under the  License is
distributed on an  "AS IS" BASIS,  WITHOUT WARRANTIES
OR CONDITIONS OF ANY KIND, either express or implied.
See the  License for the specific  language governing
permissions and limitations under the License.
"""
# VerticaPy Modules
from verticapy.utils._decorators import save_verticapy_logs
from verticapy.sql.read import _executeSQL
from verticapy.errors import ExtensionError


@save_verticapy_logs
def read_shp(
    path: str, schema: str = "public", table_name: str = "",
):
    """
Ingests a SHP file. For the moment, only files located in the Vertica server 
can be ingested.

Parameters
----------
path: str
    Absolute path where the SHP file is located.
schema: str, optional
    Schema where the SHP file will be ingested.
table_name: str, optional
    Final relation name.

Returns
-------
vDataFrame
    The vDataFrame of the relation.
    """
    file = path.split("/")[-1]
    file_extension = file[-3 : len(file)]
    if file_extension != "shp":
        raise ExtensionError("The file extension is incorrect !")
    query = (
        f"SELECT /*+LABEL('utilities.read_shp')*/ STV_ShpCreateTable(USING PARAMETERS file='{path}')"
        " OVER() AS create_shp_table;"
    )
    result = _executeSQL(query, title="Getting SHP definition.", method="fetchall")
    if not (table_name):
        table_name = file[:-4]
    result[0] = [f'CREATE TABLE "{schema}"."{table_name}"(']
    result = [elem[0] for elem in result]
    result = "".join(result)
    _executeSQL(result, title="Creating the relation.")
    query = (
        f'COPY "{schema}"."{table_name}" WITH SOURCE STV_ShpSource(file=\'{path}\')'
        " PARSER STV_ShpParser();"
    )
    _executeSQL(query, title="Ingesting the data.")
    print(f'The table "{schema}"."{table_name}" has been successfully created.')
    from verticapy import vDataFrame

    return vDataFrame(table_name, schema=schema)
