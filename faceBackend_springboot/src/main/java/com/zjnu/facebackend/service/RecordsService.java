package com.zjnu.facebackend.service;

import com.zjnu.facebackend.pojo.Records;
import com.baomidou.mybatisplus.extension.service.IService;
import com.zjnu.facebackend.utils.Page;
import com.zjnu.facebackend.utils.R;

/**
* @author April in lie
* @description 针对表【records】的数据库操作Service
* @createDate 2023-04-13 11:44:16
*/
public interface RecordsService extends IService<Records> {


    R getRecordsPage(Page page);
}
