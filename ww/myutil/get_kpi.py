# @Date    : 2022/6/25
# @Author  : Jin chunlong (chunlong.jin@westwell-lab.com)
# @Project : 
# @File : 
# @Software:
import requests
from ww.myutil.FileSetting import *


def request_get(url_arg, param):
    ret = requests.get(url_arg, param, timeout=10)
    return ret


def get_param(mode, start_time, end_time):
    return {'mode': mode, 'start_time': start_time, 'end_time': end_time}


def get_request_list(url_args, mode, start_time, end_time):
    param = get_param(mode, start_time, end_time)
    ret = request_get(url_args, param)
    rets = ret.content.decode('utf-8')
    result = rets.split("\n")
    ret.close()
    return result


def get_seq(curr_seqs, res_seqs):
    new_list = list()
    for curr in curr_seqs:
        res = res_seqs[0].split(',')
        if curr == '':
            new_list.append('none')
        else:
            for seq in res:
                if curr == seq:
                    new_list.append(str(res.index(seq)))
    return new_list


def get_new_res(res, seqs):
    result = list()
    for r in res:
        if len(r) != 0 and res.index(r) > 0:
            new_list = list()
            line = r.split(',')
            for seq in seqs:
                if seq != 'none':
                    new_list.append(line[int(seq)])
                else:
                    new_list.append('')
            result.append(new_list)
    return result


def get_all(start_time, end_time, vessel_id):
    conf = get_conf('conf', 'kpi')
    load_Seq = str(conf['loadSeq']).split(',')
    dsch_Seq = str(conf['dschSeq']).split(',')
    url = conf['url']
    res_load = get_request_list(url, 'LOAD', start_time, end_time)
    res_dsch = get_request_list(url, 'DSCH', start_time, end_time)
    load_seqs = get_seq(load_Seq, res_load)
    dsch_seqs = get_seq(dsch_Seq, res_dsch)
    dsch_data = get_new_res(res_dsch, dsch_seqs)
    load_data = get_new_res(res_load, load_seqs)
    numb = 1
    result = list()
    title = ["ID","VEHICLE_PLATE,TOS_RECEIVE_DISPATCH,MISSION_RECEIVE_DISPATCH,VPB_ARRIVE,VPB_FINISHED,QCTP_X_ARRIVED,QCTP_ARRIVED,QC_ALIGNED_START,QC_ALIGNED_FINISHED,RECEIVE_FINISHED,QPB_ARRIVE,QPB_FINISHED,LOCK_ARRIVED,LOCK_FINISHED,HPB_ARRIVE,HPB_FINISHED,CONTAINER_ID_1,CONTAINER_ID_2,TOS_DELIVER_DISPATCH_1,MISSION_DELIVER_DISPATCH_1,TP_ARRIVED_1,TP_ALIGNED_1_START,TP_ALIGNED_1_FINISHED,TP_FINISHED_1,TOS_DELIVER_DISPATCH_2,MISSION_DELIVER_DISPATCH_2,TP_ARRIVED_2,TP_ALIGNED_2_START,TP_ALIGNED_2_FINISHED,TP_FINISHED_2,BATTERY,ALL_TIME,VISIT_ID,SPEED,RECEIVE_MILEAGE,DELIVER_MILEAGE,TASK_TYPE,QCFT_TIME"]
    # result.append(title)
    for rs in dsch_data:
        if vessel_id in rs:
            rs.insert(0, numb)
            numb += 1
            result.append(rs)
    for rt in load_data:
        if vessel_id in rt:
            rt.insert(0, numb)
            numb += 1
            result.append(rt)

    return result


#http://172.29.60.38:8090/vehicle_data/task_flow/write_to_csv
# #http://172.31.2.62:8090/vehicle_data/docs#/
# data = get_all('2022-06-24 00:00:00', '2022-06-25 00:00:00', '')
# print(len(data))
# print(data)
