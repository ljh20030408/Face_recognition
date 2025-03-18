package com.zjnu.facebackend.mapper;


import com.zjnu.facebackend.pojo.Info;
import org.apache.ibatis.annotations.Mapper;

import java.util.List;

/**
* @author April in lie
* @description 针对表【info】的数据库操作Mapper
* @createDate 2023-04-12 16:29:05
* @Entity com/zjnu/facebackend.pojo.Info
*/
@Mapper
public interface InfoMapper {

    List<Info> getAll();

    Boolean deleteById(Long id);
}




