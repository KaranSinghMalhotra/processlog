import dsconnect as d, pandas

def logging(file, connid, table,logtimestamp, etl_runid, loglevel, processname, processstage, processsubstage, logmessage, recordcount, logerror):
 df = pandas.read_csv(file)
 con = d.config_df(df)
 print('connection done')
 query = "Insert into " + table + " values ('" + logtimestamp + "'," + str(etl_runid) + "," + str(loglevel) + ",'" + processname + "','" + processstage + "','" + processsubstage + "','" + logmessage + "'," + str(recordcount) + ",'" + logerror + "');"
 #query = "Insert into development.processlog_ss values ('" + logtimestamp + "'," + str(etl_runid) + "," + str(loglevel) + ",'" + processname + "','" + processstage + "','" + processsubstage + "','" + logmessage + "'," + str(recordcount) + ",'" + logerror + "');"
 #query = "Insert into development.processlog_ss values (logtimestamp,etl_runid,loglevel,processname,processstage,processsubstage,logmessage,recordcount,logerror);"
 df1 = con.redshift(connid, query)

 print("Query Executed")