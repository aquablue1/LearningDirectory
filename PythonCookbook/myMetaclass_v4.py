import struct


class StructField:
    """
    Descriptor representing a simple structure field
    """

    def __init__(self, format, offset):
        self.format = format
        self.offset = offset

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            r = struct.unpack_from(self.format, instance._buffer, self.offset)
            return r[0] if len(r) == 1 else r


class NestedStruct:
    """
    Descriptor representing a nested structure.
    """

    def __init__(self, name, struct_type, offset):
        self.name = name
        self.struct_type = struct_type
        self.offset = offset

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            data = instance._buffer[self.offset
            :self.offset + self.struct_type.struct_size]
            result = self.struct_type(data)
            # Save resulting structure back on instance to avoid
            # futher recomputation of this step
            setattr(instance, self.name, result)
            return result


class StructureMeta(type):
    """
    Mateclass that automtically creates StructField descriptors
    """

    def __init__(self, clsname, bases, clsdict):
        fields = getattr(self, '_fields_', [])
        # print(fields)
        byte_order = ''
        offset = 0
        for format, fieldname in fields:
            if isinstance(format, StructureMeta):
                setattr(self, fieldname, NestedStruct(fieldname, format, offset))
                offset  += format.struct_size
            else:
                if format.startswith(('<', '>', '!', '@')):
                    byte_order = format[0]
                    format = format[1:]
                format = byte_order + format
                setattr(self, fieldname, StructField(format, offset))
                offset += struct.calcsize(format)
        setattr(self, 'struct_size', offset)


class Structure(metaclass=StructureMeta):
    def __init__(self, bytedata):
        self._buffer = bytedata
        print("")

    @classmethod
    def from_file(cls, f):
        return cls(f.read(cls.struct_size))


class Point(Structure):
    _fields_ = [
        ('<d', 'x'),
        ('d', 'y')
    ]


class PolyHeader(Structure):
    _fields_ = [
        ('<i', 'file_code'),
        (Point, 'min'),     # nested struct
        (Point, 'max'),     # nested struct
        ('i', 'num_polys')
    ]


if __name__ == '__main__':
    print("Start")
    f = open('polys.bin', 'rb')
    phead = PolyHeader.from_file(f)
    # define a _fields_ and run from_file.
    print(phead.__class__)
    print(phead.min)
    print(phead.min.x)
