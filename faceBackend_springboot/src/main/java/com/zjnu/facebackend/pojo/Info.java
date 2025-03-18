package com.zjnu.facebackend.pojo;

import java.io.Serializable;

import java.util.Date;
import lombok.Data;

/**
* 
* @TableName info
*/
@Data
public class Info implements Serializable {

    private Integer id;

    private Date time;

    private String name;

    private String ip;


}
