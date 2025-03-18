package com.zjnu.facebackend.mapper;

import com.zjnu.facebackend.pojo.Records;
import com.baomidou.mybatisplus.core.mapper.BaseMapper;
import com.zjnu.facebackend.utils.Page;
import org.apache.ibatis.annotations.Mapper;

import java.util.List;

/**
* @author April in lie
* @description 针对表【records】的数据库操作Mapper
* @createDate 2023-04-13 11:44:16
* @Entity com.zjnu.facebackend.pojo.Records
*/
@Mapper
public interface RecordsMapper extends BaseMapper<Records> {

    List<Records> getRecordsPage();
}




