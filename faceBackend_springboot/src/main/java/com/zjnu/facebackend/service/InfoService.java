package com.zjnu.facebackend.service;


import com.zjnu.facebackend.pojo.Info;
import com.zjnu.facebackend.utils.Page;
import com.zjnu.facebackend.utils.R;

import java.util.List;

/**
* @author April in lie
* @description 针对表【info】的数据库操作Service
* @createDate 2023-04-12 16:29:05
*/
public interface InfoService{

    R getAll(Page page);

    R deleteById(Long id);
}
