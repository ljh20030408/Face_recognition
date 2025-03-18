package com.zjnu.facebackend.service.impl;

import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import com.github.pagehelper.PageHelper;
import com.github.pagehelper.PageInfo;
import com.zjnu.facebackend.pojo.Records;
import com.zjnu.facebackend.service.RecordsService;
import com.zjnu.facebackend.mapper.RecordsMapper;
import com.zjnu.facebackend.utils.Page;
import com.zjnu.facebackend.utils.R;
import org.springframework.stereotype.Service;

import javax.annotation.Resource;
import java.util.List;

/**
* @author April in lie
* @description 针对表【records】的数据库操作Service实现
* @createDate 2023-04-13 11:44:16
*/
@Service
public class RecordsServiceImpl extends ServiceImpl<RecordsMapper, Records>
    implements RecordsService{

    @Resource
    RecordsMapper recordsMapper;

    @Override
    public R getRecordsPage(Page page) {
        Integer currentPage = page.getCurrentPage();
        Integer pageSize = page.getPageSize();
        PageHelper.startPage(currentPage,pageSize);

        List<Records> recordsPage = recordsMapper.getRecordsPage();
        PageInfo<Records> pageInfo = new PageInfo<>(recordsPage);

        R r = new R<>();
        R success = r.success(pageInfo);
        return success;



    }
}




